# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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
from tencentcloud.apigateway.v20180808 import models


class ApigatewayClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'apigateway.tencentcloudapi.com'
    _service = 'apigateway'


    def AttachPlugin(self, request):
        """绑定插件到API上。

        :param request: Request instance for AttachPlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.AttachPluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.AttachPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.AttachPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindApiApp(self, request):
        """本接口（BindApiApp）用于绑定应用到API。

        :param request: Request instance for BindApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.BindApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindEnvironment(self, request):
        """本接口（BindEnvironment）用于绑定使用计划到服务或API。
        用户在发布服务到某个环境中后，如果 API 需要鉴权，还需要绑定使用计划才能进行调用，此接口用户将使用计划绑定到特定环境。
        目前支持绑定使用计划到API，但是同一个服务不能同时存在绑定到服务的使用计划和绑定到API的使用计划，所以对已经绑定过服务级别使用计划的环境，请先使用 服务级别使用计划降级 接口进行降级操作。

        :param request: Request instance for BindEnvironment.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindEnvironmentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.BindEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindIPStrategy(self, request):
        """本接口（BindIPStrategy）用于API绑定IP策略。

        :param request: Request instance for BindIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.BindIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindSecretIds(self, request):
        """本接口（BindSecretIds）用于为使用计划绑定密钥。
        将密钥绑定到某个使用计划，并将此使用计划绑定到某个服务发布的环境上，调用者方可使用此密钥调用这个服务中的 API，可使用本接口为使用计划绑定密钥。

        :param request: Request instance for BindSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindSecretIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSecretIds", params, headers=headers)
            response = json.loads(body)
            model = models.BindSecretIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindSubDomain(self, request):
        """本接口（BindSubDomain）用于绑定自定义域名到服务。
        API 网关中每个服务都会提供一个默认的域名供用户调用，但当用户想使用自己的已有域名时，也可以将自定义域名绑定到此服务，在做好备案、与默认域名的 CNAME 后，可直接调用自定义域名。

        :param request: Request instance for BindSubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BindSubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BindSubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.BindSubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BuildAPIDoc(self, request):
        """构建 API 文档

        :param request: Request instance for BuildAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.BuildAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.BuildAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BuildAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.BuildAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAPIDoc(self, request):
        """创建 API 文档

        :param request: Request instance for CreateAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApi(self, request):
        """本接口（CreateApi）用于创建 API 接口，创建 API 前，用户需要先创建服务，每个 API 都有自己归属的服务。

        :param request: Request instance for CreateApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApi", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApiApp(self, request):
        """本接口（CreateApiApp）用于创建应用。

        :param request: Request instance for CreateApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateApiKey(self, request):
        """本接口（CreateApiKey）用于创建一对新的 API 密钥。

        :param request: Request instance for CreateApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateApiKeyResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIPStrategy(self, request):
        """本接口（CreateIPStrategy）用于创建服务IP策略。

        :param request: Request instance for CreateIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePlugin(self, request):
        """创建API网关插件。

        :param request: Request instance for CreatePlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreatePluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreatePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateService(self, request):
        """本接口（CreateService）用于创建服务。
        API 网关使用的最大单元为服务，每个服务中可创建多个 API 接口。每个服务有一个默认域名供客户调用，用户也可绑定自定义域名到此服务中。

        :param request: Request instance for CreateService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUpstream(self, request):
        """用于创建后端通道

        :param request: Request instance for CreateUpstream.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateUpstreamRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUsagePlan(self, request):
        """本接口（CreateUsagePlan）用于创建使用计划。
        用户在使用 API 网关时，需要创建使用计划并将其绑定到服务的环境中使用。

        :param request: Request instance for CreateUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.CreateUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.CreateUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAPIDoc(self, request):
        """删除 API 文档

        :param request: Request instance for DeleteAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApi(self, request):
        """本接口（DeleteApi）用于删除已经创建的API。

        :param request: Request instance for DeleteApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApi", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApiApp(self, request):
        """本接口（DeleteApiApp）用于删除已经创建的应用。

        :param request: Request instance for DeleteApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteApiKey(self, request):
        """本接口（DeleteApiKey）用于删除一对 API 密钥。

        :param request: Request instance for DeleteApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteApiKeyResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIPStrategy(self, request):
        """本接口（DeleteIPStrategy）用于删除服务IP策略。

        :param request: Request instance for DeleteIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePlugin(self, request):
        """删除API网关插件

        :param request: Request instance for DeletePlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeletePluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeletePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteService(self, request):
        """本接口（DeleteService）用于删除 API 网关中某个服务。

        :param request: Request instance for DeleteService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceSubDomainMapping(self, request):
        """本接口（DeleteServiceSubDomainMapping）用于删除服务中某个环境的自定义域名映射。
        当用户使用自定义域名，并使用了自定义映射时，可使用此接口。但需注意，若删除了所有环境的映射时，调用此 API 均会返回失败。

        :param request: Request instance for DeleteServiceSubDomainMapping.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceSubDomainMappingRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteServiceSubDomainMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceSubDomainMapping", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceSubDomainMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUpstream(self, request):
        """删除后端通道，需要注意有API绑定时，不允许删除

        :param request: Request instance for DeleteUpstream.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteUpstreamRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUsagePlan(self, request):
        """本接口（DeleteUsagePlan）用于删除使用计划。

        :param request: Request instance for DeleteUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DeleteUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DeleteUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DemoteServiceUsagePlan(self, request):
        """本接口（DemoteServiceUsagePlan）用于将某个服务在某个环境的使用计划，降级到API上。
        如果服务内没有API不允许进行此操作。
        如果当前环境没有发布，不允许进行此操作。

        :param request: Request instance for DemoteServiceUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DemoteServiceUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DemoteServiceUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DemoteServiceUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DemoteServiceUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAPIDocDetail(self, request):
        """查询 API 文档详情

        :param request: Request instance for DescribeAPIDocDetail.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocDetailRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIDocDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIDocDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAPIDocs(self, request):
        """查询 API 文档列表

        :param request: Request instance for DescribeAPIDocs.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeAPIDocsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAPIDocs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAPIDocsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAllPluginApis(self, request):
        """展示插件相关的API列表，包括已绑定的和未绑定的API信息。

        :param request: Request instance for DescribeAllPluginApis.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeAllPluginApisRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeAllPluginApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAllPluginApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAllPluginApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApi(self, request):
        """本接口（DescribeApi）用于查询用户 API 网关的 API 接口的详细信息。​

        :param request: Request instance for DescribeApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApi", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiApp(self, request):
        """本接口（DescribeApiApp）用于根据应用ID搜索应用。

        :param request: Request instance for DescribeApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiAppBindApisStatus(self, request):
        """本接口（DescribeApiAppBindApisStatus）查询应用绑定的Api列表。

        :param request: Request instance for DescribeApiAppBindApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppBindApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppBindApisStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiAppBindApisStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiAppBindApisStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiAppsStatus(self, request):
        """本接口（DescribeApiAppsStatus）查询应用列表。

        :param request: Request instance for DescribeApiAppsStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppsStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiAppsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiAppsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiAppsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiBindApiAppsStatus(self, request):
        """本接口（DescribeApiBindApiAppsStatus）查询Api绑定的应用列表。

        :param request: Request instance for DescribeApiBindApiAppsStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiBindApiAppsStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiBindApiAppsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiBindApiAppsStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiBindApiAppsStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiEnvironmentStrategy(self, request):
        """本接口（DescribeApiEnvironmentStrategy）用于展示API绑定的限流策略。

        :param request: Request instance for DescribeApiEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiForApiApp(self, request):
        """本接口（DescribeApiForApiApp）用于应用使用者查询部署于 API 网关的 API 接口的详细信息。​

        :param request: Request instance for DescribeApiForApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiForApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiForApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiForApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiForApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiKey(self, request):
        """本接口（DescribeApiKey）用于查询密钥详情。
        用户在创建密钥后，可用此接口查询一个 API 密钥的详情，该接口会显示密钥 Key。

        :param request: Request instance for DescribeApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiKeysStatus(self, request):
        """本接口（DescribeApiKeysStatus）用于查询密钥列表。
        当用户创建了多个密钥对时，可使用本接口查询一个或多个 API 密钥信息。

        :param request: Request instance for DescribeApiKeysStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeysStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiKeysStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiKeysStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiKeysStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApiUsagePlan(self, request):
        """本接口（DescribeApiUsagePlan）用于查询服务中 API 使用计划详情。
        服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务及其中 API 的所有使用计划。

        :param request: Request instance for DescribeApiUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApiUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApisStatus(self, request):
        """本接口（DescribeApisStatus）用于查看一个服务下的某个 API 或所有 API 列表及其相关信息。

        :param request: Request instance for DescribeApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApisStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApisStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExclusiveInstanceDetail(self, request):
        """本接口（DescribeExclusiveInstanceDetail）用于查询独享实例详情信息。

        :param request: Request instance for DescribeExclusiveInstanceDetail.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstanceDetailRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExclusiveInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExclusiveInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExclusiveInstances(self, request):
        """本接口（DescribeExclusiveInstances）用于查询独享实例列表信息。

        :param request: Request instance for DescribeExclusiveInstances.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstancesRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExclusiveInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExclusiveInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExclusiveInstancesStatus(self, request):
        """查询专享实例列表（新）

        :param request: Request instance for DescribeExclusiveInstancesStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstancesStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstancesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExclusiveInstancesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExclusiveInstancesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIPStrategy(self, request):
        """本接口（DescribeIPStrategy）用于查询IP策略详情。

        :param request: Request instance for DescribeIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIPStrategyApisStatus(self, request):
        """本接口（DescribeIPStrategyApisStatus）用于查询IP策略可以绑定的API列表。即服务下所有API和该策略已绑定API的差集。

        :param request: Request instance for DescribeIPStrategyApisStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyApisStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategyApisStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStrategyApisStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStrategyApisStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIPStrategysStatus(self, request):
        """本接口（DescribeIPStrategysStatus）用于查询服务IP策略列表，因为接口名拼写错误，已不推荐使用，请优先使用DescribeIPStrategiesStatus接口。

        :param request: Request instance for DescribeIPStrategysStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategysStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeIPStrategysStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPStrategysStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPStrategysStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogSearch(self, request):
        """本接口DescribeLogSearch用于搜索日志

        :param request: Request instance for DescribeLogSearch.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeLogSearchRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeLogSearchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogSearch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogSearchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePlugin(self, request):
        """展示插件详情，支持按照插件ID进行。

        :param request: Request instance for DescribePlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePluginApis(self, request):
        """查询指定插件下绑定的API信息

        :param request: Request instance for DescribePluginApis.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginApisRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePlugins(self, request):
        """展示插件列表和详情，支持分页，支持按照插件类型查询，支持按照插件ID批量查询，支持按照插件名称查询。

        :param request: Request instance for DescribePlugins.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlugins", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePluginsByApi(self, request):
        """展示API上已绑定的插件列表。

        :param request: Request instance for DescribePluginsByApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginsByApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribePluginsByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePluginsByApi", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePluginsByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeService(self, request):
        """本接口（DescribeService）用于查询一个服务的详细信息、包括服务的描述、域名、协议、创建时间、发布情况等信息。

        :param request: Request instance for DescribeService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceEnvironmentList(self, request):
        """本接口（DescribeServiceEnvironmentList）用于查询一个服务的环境列表，可查询到此服务下所有环境及其状态。

        :param request: Request instance for DescribeServiceEnvironmentList.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentListRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceEnvironmentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceEnvironmentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceEnvironmentReleaseHistory(self, request):
        """本接口（DescribeServiceEnvironmentReleaseHistory）用于查询服务环境的发布历史。
        用户在创建好服务后需要发布到某个环境中才能进行使用，本接口用于查询一个服务某个环境的发布记录。

        :param request: Request instance for DescribeServiceEnvironmentReleaseHistory.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentReleaseHistoryRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentReleaseHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceEnvironmentReleaseHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceEnvironmentReleaseHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceEnvironmentStrategy(self, request):
        """本接口（DescribeServiceEnvironmentStrategy）用于展示服务限流策略。

        :param request: Request instance for DescribeServiceEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceForApiApp(self, request):
        """本接口（DescribeServiceForApiApp）用于应用使用者查询一个服务的详细信息、包括服务的描述、域名、协议等信息。

        :param request: Request instance for DescribeServiceForApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceForApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceForApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceForApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceForApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceReleaseVersion(self, request):
        """本接口（DescribeServiceReleaseVersion）查询一个服务下面所有已经发布的版本列表。
        用户在发布服务时，常有多个版本发布，可使用本接口查询已发布的版本。

        :param request: Request instance for DescribeServiceReleaseVersion.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceReleaseVersionRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceReleaseVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceReleaseVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceReleaseVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceSubDomainMappings(self, request):
        """本接口（DescribeServiceSubDomainMappings）用于查询自定义域名的路径映射。
        API 网关可绑定自定义域名到服务，并且可以对自定义域名的路径进行映射，可自定义不同的路径映射到服务中的三个环境，本接口用于查询绑定服务的自定义域名的路径映射列表。

        :param request: Request instance for DescribeServiceSubDomainMappings.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainMappingsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainMappingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceSubDomainMappings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceSubDomainMappingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceSubDomains(self, request):
        """本接口（DescribeServiceSubDomains）用于查询自定义域名列表。
        API 网关可绑定自定义域名到服务，用于服务调用。此接口用于查询用户绑定在服务的自定义域名列表。

        :param request: Request instance for DescribeServiceSubDomains.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceSubDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceSubDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceSubDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceUsagePlan(self, request):
        """本接口（DescribeServiceUsagePlan）用于查询服务使用计划详情。
        服务若需要鉴权限流生效，则需要绑定使用计划到此服务中，本接口用于查询绑定到一个服务的所有使用计划。

        :param request: Request instance for DescribeServiceUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServiceUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServicesStatus(self, request):
        """本接口（DescribeServicesStatus）用于搜索查询某一个服务或多个服务的列表，并返回服务相关的域名、时间等信息。

        :param request: Request instance for DescribeServicesStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeServicesStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeServicesStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServicesStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServicesStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUpstreamBindApis(self, request):
        """查询后端通道所绑定的API列表

        :param request: Request instance for DescribeUpstreamBindApis.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApisRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpstreamBindApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpstreamBindApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUpstreams(self, request):
        """查询后端通道列表详情

        :param request: Request instance for DescribeUpstreams.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpstreams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpstreamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsagePlan(self, request):
        """本接口（DescribeUsagePlan）用于查询一个使用计划的详细信息，包括名称、QPS、创建时间绑定的环境等。

        :param request: Request instance for DescribeUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsagePlanEnvironments(self, request):
        """本接口（DescribeUsagePlanEnvironments）用于查询使用计划绑定的环境列表。
        用户在绑定了某个使用计划到环境后，可使用本接口查询这个使用计划绑定的所有服务的环境。

        :param request: Request instance for DescribeUsagePlanEnvironments.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanEnvironmentsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlanEnvironments", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlanEnvironmentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsagePlanSecretIds(self, request):
        """本接口（DescribeUsagePlanSecretIds）用于查询使用计划绑定的密钥列表。
        在 API 网关中，一个使用计划可绑定多个密钥对，可使用本接口查询使用计划绑定的密钥列表。

        :param request: Request instance for DescribeUsagePlanSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlanSecretIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlanSecretIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlanSecretIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsagePlansStatus(self, request):
        """本接口（DescribeUsagePlanStatus）用于查询使用计划的列表。

        :param request: Request instance for DescribeUsagePlansStatus.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlansStatusRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DescribeUsagePlansStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsagePlansStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsagePlansStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachPlugin(self, request):
        """解除插件与API绑定

        :param request: Request instance for DetachPlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DetachPluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DetachPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.DetachPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableApiKey(self, request):
        """本接口（DisableApiKey）用于禁用一对 API 密钥。

        :param request: Request instance for DisableApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.DisableApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.DisableApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DisableApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableApiKey(self, request):
        """本接口（EnableApiKey）用于启动一对被禁用的 API 密钥。

        :param request: Request instance for EnableApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.EnableApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.EnableApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.EnableApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateApiDocument(self, request):
        """接口已废弃

        本接口（GenerateApiDocument）用于自动生成 API 文档和 SDK，一个服务的一个环境生成一份文档和 SDK。

        :param request: Request instance for GenerateApiDocument.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.GenerateApiDocumentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.GenerateApiDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateApiDocument", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateApiDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportOpenApi(self, request):
        """本接口（ImportOpenApi）用于将OpenAPI规范定义的API导入到API网关。

        :param request: Request instance for ImportOpenApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ImportOpenApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ImportOpenApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportOpenApi", params, headers=headers)
            response = json.loads(body)
            model = models.ImportOpenApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAPIDoc(self, request):
        """修改 API 文档

        :param request: Request instance for ModifyAPIDoc.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyAPIDocRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyAPIDocResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAPIDoc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAPIDocResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApi(self, request):
        """本接口（ModifyApi）用于修改 API 接口，可调用此接口对已经配置的 API 接口进行编辑修改。修改后的 API 需要重新发布 API 所在的服务到对应环境方能生效。

        :param request: Request instance for ModifyApi.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApi", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApiApp(self, request):
        """本接口（ModifyApiApp）用于修改已经创建的应用。

        :param request: Request instance for ModifyApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApiEnvironmentStrategy(self, request):
        """本接口（ModifyApiEnvironmentStrategy）用于修改API限流策略

        :param request: Request instance for ModifyApiEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApiIncrement(self, request):
        """提供增量更新API能力，主要是给程序调用（区别于ModifyApi，该接口是需要传入API的全量参数，对console使用较友好）

        :param request: Request instance for ModifyApiIncrement.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiIncrementRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyApiIncrementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApiIncrement", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyApiIncrementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyExclusiveInstance(self, request):
        """本接口（ModifyExclusiveInstance）用于修改独享实例信息。​

        :param request: Request instance for ModifyExclusiveInstance.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyExclusiveInstanceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyExclusiveInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExclusiveInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExclusiveInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIPStrategy(self, request):
        """本接口（ModifyIPStrategy）用于修改服务IP策略。

        :param request: Request instance for ModifyIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPlugin(self, request):
        """修改API网关插件。

        :param request: Request instance for ModifyPlugin.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyPluginRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyPluginResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPlugin", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPluginResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyService(self, request):
        """本接口（ModifyService）用于修改服务的相关信息。当服务创建后，服务的名称、描述和服务类型均可被修改。

        :param request: Request instance for ModifyService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceEnvironmentStrategy(self, request):
        """本接口（ModifyServiceEnvironmentStrategy）用于修改服务限流策略

        :param request: Request instance for ModifyServiceEnvironmentStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceEnvironmentStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyServiceEnvironmentStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceEnvironmentStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceEnvironmentStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubDomain(self, request):
        """本接口（ModifySubDomain）用于修改服务的自定义域名设置中的路径映射，可以修改绑定自定义域名之前的路径映射规则。

        :param request: Request instance for ModifySubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifySubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifySubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUpstream(self, request):
        """修改后端通道

        :param request: Request instance for ModifyUpstream.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyUpstreamRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyUpstreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUpstream", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUpstreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUsagePlan(self, request):
        """本接口（ModifyUsagePlan）用于修改使用计划的名称，描述及 QPS。

        :param request: Request instance for ModifyUsagePlan.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ModifyUsagePlanRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ModifyUsagePlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUsagePlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUsagePlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseService(self, request):
        """本接口（ReleaseService）用于发布服务。
        API 网关的服务创建后，需要发布到某个环境方生效后，使用者才能进行调用，此接口用于发布服务到环境，如 release 环境。

        :param request: Request instance for ReleaseService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ReleaseServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ReleaseServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseService", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAPIDocPassword(self, request):
        """重置API文档密码

        :param request: Request instance for ResetAPIDocPassword.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.ResetAPIDocPasswordRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.ResetAPIDocPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAPIDocPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAPIDocPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindEnvironment(self, request):
        """本接口（UnBindEnvironment）用于将使用计划从特定环境解绑。

        :param request: Request instance for UnBindEnvironment.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindEnvironmentRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindEnvironment", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindEnvironmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindIPStrategy(self, request):
        """本接口（UnBindIPStrategy）用于服务解绑IP策略。

        :param request: Request instance for UnBindIPStrategy.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindIPStrategyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindIPStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindIPStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindIPStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindSecretIds(self, request):
        """本接口（UnBindSecretIds）用于为使用计划解绑密钥。

        :param request: Request instance for UnBindSecretIds.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindSecretIdsRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindSecretIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindSecretIds", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindSecretIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnBindSubDomain(self, request):
        """本接口（UnBindSubDomain）用于解绑自定义域名。
        用户使用 API 网关绑定了自定义域名到服务中后，若想要解绑此自定义域名，可使用此接口。

        :param request: Request instance for UnBindSubDomain.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnBindSubDomainRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnBindSubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnBindSubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.UnBindSubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnReleaseService(self, request):
        """本接口（UnReleaseService）用于下线服务。
        用户发布服务到某个环境后，此服务中的 API 方可被调用者进行调用，当用户需要将此服务从发布环境中下线时，可调用此 API。下线后的服务不可被调用。

        :param request: Request instance for UnReleaseService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnReleaseServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnReleaseServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnReleaseService", params, headers=headers)
            response = json.loads(body)
            model = models.UnReleaseServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindApiApp(self, request):
        """本接口（UnbindApiApp）用于解除应用和API绑定。

        :param request: Request instance for UnbindApiApp.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UnbindApiAppRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UnbindApiAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindApiApp", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindApiAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateApiAppKey(self, request):
        """本接口（UpdateApiAppKey）用于更新应用密钥。

        :param request: Request instance for UpdateApiAppKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiAppKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiAppKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiAppKey", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiAppKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateApiKey(self, request):
        """本接口（UpdateApiKey）用于更换用户已创建的一对 API 密钥。

        :param request: Request instance for UpdateApiKey.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiKeyRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateService(self, request):
        """本接口（UpdateService）用于从服务已发布的环境中将运行版本切换到特定版本。用户在使用 API 网关创建服务并发布服务到某个环境后，如在开发过程产生多个版本需要切换，此时可调用本接口。

        :param request: Request instance for UpdateService.
        :type request: :class:`tencentcloud.apigateway.v20180808.models.UpdateServiceRequest`
        :rtype: :class:`tencentcloud.apigateway.v20180808.models.UpdateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateService", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)