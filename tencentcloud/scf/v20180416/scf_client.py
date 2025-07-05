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
from tencentcloud.scf.v20180416 import models


class ScfClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'scf.tencentcloudapi.com'
    _service = 'scf'


    def CopyFunction(self, request):
        """复制一个函数，您可以选择将复制出的新函数放置在特定的Region和Namespace。
        注：本接口**不会**复制函数的以下对象或属性：
        1. 函数的触发器
        2. 除了$LATEST以外的其它版本
        3. 函数配置的日志投递到的CLS目标。

        如有需要，您可以在复制后手动配置新函数。

        :param request: Request instance for CopyFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.CopyFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CopyFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CopyFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlias(self, request):
        """为某个函数版本创建一个别名，您可以使用别名来标记特定的函数版本，如DEV/RELEASE版本，也可以随时修改别名指向的版本。
        一个别名必须指向一个主版本，此外还可以同时指向一个附加版本。调用函数时指定特定的别名，则请求会被发送到别名指向的版本上，您可以配置请求发送到主版本和附加版本的比例。

        :param request: Request instance for CreateAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomDomain(self, request):
        """创建自定义域名

        :param request: Request instance for CreateCustomDomain.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateCustomDomainRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateCustomDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFunction(self, request):
        """该接口根据传入参数创建新的函数。

        :param request: Request instance for CreateFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNamespace(self, request):
        """该接口根据传入的参数创建命名空间。

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrigger(self, request):
        """该接口根据参数输入设置新的触发方式。

        :param request: Request instance for CreateTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.CreateTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.CreateTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlias(self, request):
        """删除一个函数版本的别名

        :param request: Request instance for DeleteAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlias", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomDomain(self, request):
        """删除自定义域名

        :param request: Request instance for DeleteCustomDomain.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteCustomDomainRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteCustomDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunction(self, request):
        """该接口根据传入参数删除函数。

        :param request: Request instance for DeleteFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFunctionVersion(self, request):
        """该接口根据传入参数删除函数的指定版本。

        :param request: Request instance for DeleteFunctionVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteFunctionVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFunctionVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFunctionVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLayerVersion(self, request):
        """删除指定层的指定版本，被删除的版本无法再关联到函数上，但不会影响正在引用这个层的函数。

        :param request: Request instance for DeleteLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteLayerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLayerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLayerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNamespace(self, request):
        """该接口根据传入的参数删除命名空间。

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteProvisionedConcurrencyConfig(self, request):
        """删除函数版本的预置并发配置。

        :param request: Request instance for DeleteProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteProvisionedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteProvisionedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReservedConcurrencyConfig(self, request):
        """删除函数的最大独占配额配置。

        :param request: Request instance for DeleteReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReservedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReservedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrigger(self, request):
        """该接口根据参数传入删除已有的触发方式。

        :param request: Request instance for DeleteTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.DeleteTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAccount(self, request):
        """获取账户信息

        :param request: Request instance for GetAccount.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAccountRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAccount", params, headers=headers)
            response = json.loads(body)
            model = models.GetAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlias(self, request):
        """获取别名的详细信息，包括名称、描述、版本、路由信息等。

        :param request: Request instance for GetAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlias", params, headers=headers)
            response = json.loads(body)
            model = models.GetAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAsyncEventStatus(self, request):
        """获取函数异步执行事件状态，事件状态保留 3 * 24 小时（从事件完成开始计时）。

        :param request: Request instance for GetAsyncEventStatus.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetAsyncEventStatusRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetAsyncEventStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAsyncEventStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetAsyncEventStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCustomDomain(self, request):
        """查看云函数自定义域名详情

        :param request: Request instance for GetCustomDomain.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetCustomDomainRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetCustomDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCustomDomain", params, headers=headers)
            response = json.loads(body)
            model = models.GetCustomDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunction(self, request):
        """该接口获取某个函数的详细信息，包括名称、代码、处理方法、关联触发器和超时时间等字段。

        :param request: Request instance for GetFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunction", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunctionAddress(self, request):
        """该接口用于获取函数代码包的下载地址。

        :param request: Request instance for GetFunctionAddress.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunctionAddress", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunctionEventInvokeConfig(self, request):
        """获取函数异步重试配置，包括重试次数和消息保留时间

        :param request: Request instance for GetFunctionEventInvokeConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionEventInvokeConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionEventInvokeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunctionEventInvokeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionEventInvokeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetFunctionLogs(self, request):
        """该接口根据指定的日志查询条件返回函数运行日志。该接口已下线，查询函数请求运行的返回信息，请使用 [GetRequestStatus](https://cloud.tencent.com/document/product/583/65348)。查询函数运行日志，请参考[日志检索教程](https://cloud.tencent.com/document/product/583/52637)。

        :param request: Request instance for GetFunctionLogs.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetFunctionLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFunctionLogs", params, headers=headers)
            response = json.loads(body)
            model = models.GetFunctionLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLayerVersion(self, request):
        """获取层版本详细信息，包括用于下载层中文件的链接。

        :param request: Request instance for GetLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetLayerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLayerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.GetLayerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetProvisionedConcurrencyConfig(self, request):
        """获取函数或函数某一版本的预置并发详情。

        :param request: Request instance for GetProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetProvisionedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetProvisionedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRequestStatus(self, request):
        """该接口根据指定的查询条件返回函数单个请求运行状态。

        :param request: Request instance for GetRequestStatus.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetRequestStatusRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetRequestStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRequestStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetRequestStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetReservedConcurrencyConfig(self, request):
        """获取函数的最大独占配额详情。

        :param request: Request instance for GetReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.GetReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.GetReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetReservedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetReservedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Invoke(self, request):
        """该接口用于运行函数。

        :param request: Request instance for Invoke.
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Invoke", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InvokeFunction(self, request):
        """SCF同步调用函数接口。

        :param request: Request instance for InvokeFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.InvokeFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.InvokeFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeFunction", params, headers=headers)
            response = json.loads(body)
            model = models.InvokeFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAliases(self, request):
        """返回一个函数下的全部别名，可以根据特定函数版本过滤。

        :param request: Request instance for ListAliases.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListAliasesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListAliasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAliases", params, headers=headers)
            response = json.loads(body)
            model = models.ListAliasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAsyncEvents(self, request):
        """拉取函数异步事件列表

        :param request: Request instance for ListAsyncEvents.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListAsyncEventsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListAsyncEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAsyncEvents", params, headers=headers)
            response = json.loads(body)
            model = models.ListAsyncEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListCustomDomains(self, request):
        """遍历域名列表信息

        :param request: Request instance for ListCustomDomains.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListCustomDomainsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListCustomDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListCustomDomains", params, headers=headers)
            response = json.loads(body)
            model = models.ListCustomDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListFunctions(self, request):
        """该接口根据传入的查询参数返回相关函数信息。

        :param request: Request instance for ListFunctions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListFunctionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.ListFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLayerVersions(self, request):
        """返回指定层的全部版本的信息

        :param request: Request instance for ListLayerVersions.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayerVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLayerVersions", params, headers=headers)
            response = json.loads(body)
            model = models.ListLayerVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLayers(self, request):
        """返回全部层的列表，其中包含了每个层最新版本的信息，可以通过适配运行时进行过滤。

        :param request: Request instance for ListLayers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListLayersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListLayersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLayers", params, headers=headers)
            response = json.loads(body)
            model = models.ListLayersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListNamespaces(self, request):
        """列出命名空间列表

        :param request: Request instance for ListNamespaces.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListNamespacesRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListNamespacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListNamespaces", params, headers=headers)
            response = json.loads(body)
            model = models.ListNamespacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTriggers(self, request):
        """获取函数触发器列表

        :param request: Request instance for ListTriggers.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListTriggersRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListTriggersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTriggers", params, headers=headers)
            response = json.loads(body)
            model = models.ListTriggersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListVersionByFunction(self, request):
        """该接口根据传入的参数查询函数的版本。

        :param request: Request instance for ListVersionByFunction.
        :type request: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.ListVersionByFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListVersionByFunction", params, headers=headers)
            response = json.loads(body)
            model = models.ListVersionByFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishLayerVersion(self, request):
        """使用给定的zip文件或cos对象创建一个层的新版本，每次使用相同的层的名称调用本接口，都会生成一个新版本。

        :param request: Request instance for PublishLayerVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishLayerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishLayerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.PublishLayerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PublishVersion(self, request):
        """该接口用于用户发布新版本函数。

        :param request: Request instance for PublishVersion.
        :type request: :class:`tencentcloud.scf.v20180416.models.PublishVersionRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PublishVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PublishVersion", params, headers=headers)
            response = json.loads(body)
            model = models.PublishVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutProvisionedConcurrencyConfig(self, request):
        """设置函数某一非$LATEST版本的预置并发。

        :param request: Request instance for PutProvisionedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutProvisionedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutProvisionedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutProvisionedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.PutProvisionedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutReservedConcurrencyConfig(self, request):
        """设置函数最大独占配额

        :param request: Request instance for PutReservedConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutReservedConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutReservedConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutReservedConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.PutReservedConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutTotalConcurrencyConfig(self, request):
        """修改账号并发限制配额

        :param request: Request instance for PutTotalConcurrencyConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.PutTotalConcurrencyConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.PutTotalConcurrencyConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutTotalConcurrencyConfig", params, headers=headers)
            response = json.loads(body)
            model = models.PutTotalConcurrencyConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateAsyncEvent(self, request):
        """终止正在运行中的函数异步事件

        :param request: Request instance for TerminateAsyncEvent.
        :type request: :class:`tencentcloud.scf.v20180416.models.TerminateAsyncEventRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.TerminateAsyncEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateAsyncEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateAsyncEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlias(self, request):
        """更新别名的配置

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCustomDomain(self, request):
        """更新自定义域名相关配置

        :param request: Request instance for UpdateCustomDomain.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateCustomDomainRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateCustomDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCustomDomain", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCustomDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFunctionCode(self, request):
        """该接口根据传入参数更新函数代码。

        :param request: Request instance for UpdateFunctionCode.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFunctionCode", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFunctionCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFunctionConfiguration(self, request):
        """该接口根据传入参数更新函数配置。

        :param request: Request instance for UpdateFunctionConfiguration.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFunctionConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFunctionConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFunctionEventInvokeConfig(self, request):
        """更新函数的异步重试配置，包括重试次数和消息保留时间

        :param request: Request instance for UpdateFunctionEventInvokeConfig.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionEventInvokeConfigRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateFunctionEventInvokeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFunctionEventInvokeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFunctionEventInvokeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateNamespace(self, request):
        """更新命名空间

        :param request: Request instance for UpdateNamespace.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTrigger(self, request):
        """支持触发器配置更新。
        默认接口请求频率限制：20次/秒

        注意：目前只支持timer触发器和ckafka触发器更新！

        timer触发器和ckafka触发器支持更新字段有：Enable、TriggerDesc、Description、CustomArgument。

        timer触发器TriggerDesc支持5段式和7段式的更新。

        ckafka触发器TriggerDesc支持Retry、MaxMsgNum、TimeOut参数更新，不传值表示原值不变，传值不能为空。

        Enable 触发器开启或关闭，传参为OPEN为开启，CLOSE为关闭。不传值表示原值不变，传值不能为空。

        Description 触发器描述，不传值保持原值不变，传值为空则为空。

        CustomArgument 触发器用户附加信息（注意：只有timer触发器展示），不传值保持原值不变，传值为空则为空。

        :param request: Request instance for UpdateTrigger.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateTriggerRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateTriggerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTrigger", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTriggerStatus(self, request):
        """更新触发器状态的值

        :param request: Request instance for UpdateTriggerStatus.
        :type request: :class:`tencentcloud.scf.v20180416.models.UpdateTriggerStatusRequest`
        :rtype: :class:`tencentcloud.scf.v20180416.models.UpdateTriggerStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTriggerStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTriggerStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))