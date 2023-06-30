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
from tencentcloud.tcb.v20180608 import models


class TcbClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'tcb.tencentcloudapi.com'
    _service = 'tcb'


    def BindEnvGateway(self, request):
        """绑定另外一个环境下的网关，callContainer请求可以访问到该网关

        :param request: Request instance for BindEnvGateway.
        :type request: :class:`tencentcloud.tcb.v20180608.models.BindEnvGatewayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.BindEnvGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindEnvGateway", params, headers=headers)
            response = json.loads(body)
            model = models.BindEnvGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckTcbService(self, request):
        """检查是否开通Tcb服务

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
                raise TencentCloudSDKException(e.message, e.message)


    def CommonServiceAPI(self, request):
        """TCB云API统一入口

        :param request: Request instance for CommonServiceAPI.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CommonServiceAPIRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CommonServiceAPIResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommonServiceAPI", params, headers=headers)
            response = json.loads(body)
            model = models.CommonServiceAPIResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAndDeployCloudBaseProject(self, request):
        """创建云开发项目

        :param request: Request instance for CreateAndDeployCloudBaseProject.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateAndDeployCloudBaseProjectRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateAndDeployCloudBaseProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndDeployCloudBaseProject", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndDeployCloudBaseProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAuthDomain(self, request):
        """增加安全域名

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCloudBaseRunResource(self, request):
        """开通容器托管的资源，包括集群创建，VPC配置，异步任务创建，镜像托管，Coding等，查看创建结果需要根据DescribeCloudBaseRunResource接口来查看

        :param request: Request instance for CreateCloudBaseRunResource.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateCloudBaseRunResourceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateCloudBaseRunResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudBaseRunResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudBaseRunResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCloudBaseRunServerVersion(self, request):
        """创建服务版本

        :param request: Request instance for CreateCloudBaseRunServerVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateCloudBaseRunServerVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateCloudBaseRunServerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudBaseRunServerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudBaseRunServerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHostingDomain(self, request):
        """创建托管域名

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePostpayPackage(self, request):
        """开通后付费资源

        :param request: Request instance for CreatePostpayPackage.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreatePostpayPackageRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreatePostpayPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePostpayPackage", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePostpayPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStandaloneGateway(self, request):
        """本接口（CreateStandaloneGateway）用于创建独立网关。

        :param request: Request instance for CreateStandaloneGateway.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateStandaloneGatewayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateStandaloneGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStandaloneGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStandaloneGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStaticStore(self, request):
        """创建静态托管资源，包括COS和CDN，异步任务创建，查看创建结果需要根据DescribeStaticStore接口来查看

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWxCloudBaseRunEnv(self, request):
        """创建微信云托管

        :param request: Request instance for CreateWxCloudBaseRunEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateWxCloudBaseRunEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateWxCloudBaseRunEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWxCloudBaseRunEnv", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWxCloudBaseRunEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWxCloudBaseRunServerDBCluster(self, request):
        """开通微信云托管MySQL数据库服务

        :param request: Request instance for CreateWxCloudBaseRunServerDBCluster.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CreateWxCloudBaseRunServerDBClusterRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CreateWxCloudBaseRunServerDBClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWxCloudBaseRunServerDBCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWxCloudBaseRunServerDBClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCloudBaseProjectLatestVersion(self, request):
        """删除云项目

        :param request: Request instance for DeleteCloudBaseProjectLatestVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseProjectLatestVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseProjectLatestVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudBaseProjectLatestVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudBaseProjectLatestVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCloudBaseRunServerVersion(self, request):
        """删除服务版本

        :param request: Request instance for DeleteCloudBaseRunServerVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseRunServerVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteCloudBaseRunServerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCloudBaseRunServerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCloudBaseRunServerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteEndUser(self, request):
        """删除终端用户

        :param request: Request instance for DeleteEndUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteEndUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteEndUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEndUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEndUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteGatewayVersion(self, request):
        """删除网关某版本

        :param request: Request instance for DeleteGatewayVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteGatewayVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteGatewayVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGatewayVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGatewayVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWxGatewayRoute(self, request):
        """删除安全网关路由

        :param request: Request instance for DeleteWxGatewayRoute.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DeleteWxGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DeleteWxGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWxGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWxGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeActivityInfo(self, request):
        """查询活动信息

        :param request: Request instance for DescribeActivityInfo.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeActivityInfoRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeActivityInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActivityInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActivityInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeActivityRecord(self, request):
        """查询活动记录信息

        :param request: Request instance for DescribeActivityRecord.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeActivityRecordRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeActivityRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActivityRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActivityRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAuthDomains(self, request):
        """获取安全域名列表

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBaasPackageList(self, request):
        """获取新套餐列表，含详情，如果传了PackageId，则只获取指定套餐详情

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBillingInfo(self, request):
        """获取计费相关信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCbrServerVersion(self, request):
        """查询服务版本的详情

        :param request: Request instance for DescribeCbrServerVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCbrServerVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCbrServerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCbrServerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCbrServerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseBuildService(self, request):
        """获取云托管代码上传url

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseProjectLatestVersionList(self, request):
        """获取云开发项目列表

        :param request: Request instance for DescribeCloudBaseProjectLatestVersionList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseProjectLatestVersionListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseProjectLatestVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseProjectLatestVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseProjectLatestVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseProjectVersionList(self, request):
        """云项目部署列表

        :param request: Request instance for DescribeCloudBaseProjectVersionList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseProjectVersionListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseProjectVersionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseProjectVersionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseProjectVersionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunAllVpcs(self, request):
        """查询环境下所有的vpc列表

        :param request: Request instance for DescribeCloudBaseRunAllVpcs.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunAllVpcsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunAllVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunAllVpcs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunAllVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunConfForGateWay(self, request):
        """独立网关中拉取云托管服务对应的配置信息

        :param request: Request instance for DescribeCloudBaseRunConfForGateWay.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunConfForGateWayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunConfForGateWayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunConfForGateWay", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunConfForGateWayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunOneClickTaskExternal(self, request):
        """查询一键部署任务 （特定接口：外部查询使用）

        :param request: Request instance for DescribeCloudBaseRunOneClickTaskExternal.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunOneClickTaskExternalRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunOneClickTaskExternalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunOneClickTaskExternal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunOneClickTaskExternalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunOperationTypes(self, request):
        """查询服务、版本和操作类型

        :param request: Request instance for DescribeCloudBaseRunOperationTypes.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunOperationTypesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunOperationTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunOperationTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunOperationTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunPodList(self, request):
        """查询云应用服务版本容器列表

        :param request: Request instance for DescribeCloudBaseRunPodList.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunPodListRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunPodListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunPodList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunPodListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunResource(self, request):
        """查看容器托管的集群状态

        :param request: Request instance for DescribeCloudBaseRunResource.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunResourceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunResourceForExtend(self, request):
        """查看容器托管的集群状态扩展使用

        :param request: Request instance for DescribeCloudBaseRunResourceForExtend.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunResourceForExtendRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunResourceForExtendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunResourceForExtend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunResourceForExtendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunServer(self, request):
        """查询单个服务的详情，版本以及详情

        :param request: Request instance for DescribeCloudBaseRunServer.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunServerRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunServerDomainName(self, request):
        """查询微信云托管服务域名

        :param request: Request instance for DescribeCloudBaseRunServerDomainName.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunServerDomainNameRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunServerDomainNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunServerDomainName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunServerDomainNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunServerVersion(self, request):
        """查询服务版本的详情，CPU和MEM  请使用CPUSize和MemSize

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunVersion(self, request):
        """查询服务版本详情(新)

        :param request: Request instance for DescribeCloudBaseRunVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunVersionRsByCondition(self, request):
        """DescribeCloudBaseRunVersionRsByCondition 获取云托管详情

        :param request: Request instance for DescribeCloudBaseRunVersionRsByCondition.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunVersionRsByConditionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunVersionRsByConditionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunVersionRsByCondition", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunVersionRsByConditionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCloudBaseRunVersionSnapshot(self, request):
        """查询版本历史

        :param request: Request instance for DescribeCloudBaseRunVersionSnapshot.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunVersionSnapshotRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeCloudBaseRunVersionSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloudBaseRunVersionSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloudBaseRunVersionSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCurveData(self, request):
        """根据用户传入的指标, 拉取一段时间内的监控数据。

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseACL(self, request):
        """获取数据库权限

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDownloadFile(self, request):
        """获取下载文件信息

        :param request: Request instance for DescribeDownloadFile.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeDownloadFileRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeDownloadFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDownloadFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDownloadFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEndUserLoginStatistic(self, request):
        """获取环境终端用户新增与登录信息

        :param request: Request instance for DescribeEndUserLoginStatistic.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUserLoginStatisticRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUserLoginStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEndUserLoginStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEndUserLoginStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEndUserStatistic(self, request):
        """获取终端用户总量与平台分布情况

        :param request: Request instance for DescribeEndUserStatistic.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUserStatisticRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUserStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEndUserStatistic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEndUserStatisticResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEndUsers(self, request):
        """获取终端用户列表

        :param request: Request instance for DescribeEndUsers.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUsersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEndUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEndUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEndUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvDealRegion(self, request):
        """获取环境下单地域

        :param request: Request instance for DescribeEnvDealRegion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvDealRegionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvDealRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvDealRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvDealRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvFreeQuota(self, request):
        """查询后付费免费配额信息

        :param request: Request instance for DescribeEnvFreeQuota.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvFreeQuotaRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvFreeQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvFreeQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvFreeQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvLimit(self, request):
        """查询环境个数上限

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvPostpaidDeduct(self, request):
        """查询环境后付费计费详情

        :param request: Request instance for DescribeEnvPostpaidDeduct.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvPostpaidDeductRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvPostpaidDeductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvPostpaidDeduct", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnvPostpaidDeductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvs(self, request):
        """获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExtensionUploadInfo(self, request):
        """描述扩展上传文件信息

        :param request: Request instance for DescribeExtensionUploadInfo.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeExtensionUploadInfoRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeExtensionUploadInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtensionUploadInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionUploadInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExtraPkgBillingInfo(self, request):
        """获取增值包计费相关信息

        :param request: Request instance for DescribeExtraPkgBillingInfo.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeExtraPkgBillingInfoRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeExtraPkgBillingInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtraPkgBillingInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtraPkgBillingInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGatewayCurveData(self, request):
        """查询网关监控数据

        :param request: Request instance for DescribeGatewayCurveData.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeGatewayCurveDataRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeGatewayCurveDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayCurveData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayCurveDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGatewayVersions(self, request):
        """查询网关版本信息
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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGraphData(self, request):
        """根据用户传入的指标, 拉取一段时间内的监控数据。

        :param request: Request instance for DescribeGraphData.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeGraphDataRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeGraphDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGraphData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGraphDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHostingDomainTask(self, request):
        """查询静态托管域名任务状态

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePostpayFreeQuotas(self, request):
        """查询后付费资源免费量

        :param request: Request instance for DescribePostpayFreeQuotas.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribePostpayFreeQuotasRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribePostpayFreeQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostpayFreeQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostpayFreeQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePostpayPackageFreeQuotas(self, request):
        """获取后付费免费额度

        :param request: Request instance for DescribePostpayPackageFreeQuotas.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribePostpayPackageFreeQuotasRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribePostpayPackageFreeQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostpayPackageFreeQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostpayPackageFreeQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeQuotaData(self, request):
        """查询指定指标的配额使用量

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSmsQuotas(self, request):
        """查询后付费短信资源量
        1 有免费包的返回SmsFreeQuota结构所有字段
        2 没有免费包，有付费包，付费返回复用SmsFreeQuota结构，其中只有 TodayUsedQuota 字段有效
        3 都没有返回为空数组

        :param request: Request instance for DescribeSmsQuotas.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeSmsQuotasRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeSmsQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSmsQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSmsQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSpecialCostItems(self, request):
        """查询环境1分钱抵扣信息

        :param request: Request instance for DescribeSpecialCostItems.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeSpecialCostItemsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeSpecialCostItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecialCostItems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecialCostItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStandaloneGateway(self, request):
        """本接口（DescribeStandaloneGateway）查询小租户网关套餐信息。

        :param request: Request instance for DescribeStandaloneGateway.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeStandaloneGatewayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeStandaloneGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStandaloneGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStandaloneGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStandaloneGatewayPackage(self, request):
        """本接口（DescribeStandaloneGatewayPackage）用于查询小租户网关套餐信息。

        :param request: Request instance for DescribeStandaloneGatewayPackage.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeStandaloneGatewayPackageRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeStandaloneGatewayPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStandaloneGatewayPackage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStandaloneGatewayPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUserActivityInfo(self, request):
        """查询用户活动信息

        :param request: Request instance for DescribeUserActivityInfo.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeUserActivityInfoRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeUserActivityInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserActivityInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserActivityInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWxCloudBaseRunEnvs(self, request):
        """查询微信云托管环境信息

        :param request: Request instance for DescribeWxCloudBaseRunEnvs.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeWxCloudBaseRunEnvsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeWxCloudBaseRunEnvsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWxCloudBaseRunEnvs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWxCloudBaseRunEnvsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWxCloudBaseRunSubNets(self, request):
        """查询微信云托管子网

        :param request: Request instance for DescribeWxCloudBaseRunSubNets.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeWxCloudBaseRunSubNetsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeWxCloudBaseRunSubNetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWxCloudBaseRunSubNets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWxCloudBaseRunSubNetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWxGatewayRoutes(self, request):
        """查看安全网关路由

        :param request: Request instance for DescribeWxGatewayRoutes.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeWxGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeWxGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWxGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWxGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWxGateways(self, request):
        """查看安全网关

        :param request: Request instance for DescribeWxGateways.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeWxGatewaysRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeWxGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWxGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWxGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyEnv(self, request):
        """销毁环境

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
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyStandaloneGateway(self, request):
        """本接口（DestroyStandaloneGateway）用于销毁小租户网关。

        :param request: Request instance for DestroyStandaloneGateway.
        :type request: :class:`tencentcloud.tcb.v20180608.models.DestroyStandaloneGatewayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DestroyStandaloneGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyStandaloneGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyStandaloneGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyStaticStore(self, request):
        """销毁静态托管资源，该接口创建异步销毁任务，资源最终状态可从DestroyStaticStore接口查看

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
                raise TencentCloudSDKException(e.message, e.message)


    def EstablishCloudBaseRunServer(self, request):
        """创建云应用服务

        :param request: Request instance for EstablishCloudBaseRunServer.
        :type request: :class:`tencentcloud.tcb.v20180608.models.EstablishCloudBaseRunServerRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.EstablishCloudBaseRunServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EstablishCloudBaseRunServer", params, headers=headers)
            response = json.loads(body)
            model = models.EstablishCloudBaseRunServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EstablishWxGatewayRoute(self, request):
        """创建或修改安全网关路由

        :param request: Request instance for EstablishWxGatewayRoute.
        :type request: :class:`tencentcloud.tcb.v20180608.models.EstablishWxGatewayRouteRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.EstablishWxGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EstablishWxGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.EstablishWxGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FreezeCloudBaseRunServers(self, request):
        """批量冻结

        :param request: Request instance for FreezeCloudBaseRunServers.
        :type request: :class:`tencentcloud.tcb.v20180608.models.FreezeCloudBaseRunServersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.FreezeCloudBaseRunServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeCloudBaseRunServers", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeCloudBaseRunServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCloudBaseRunServerFlowConf(self, request):
        """修改容器内的版本流量配置

        :param request: Request instance for ModifyCloudBaseRunServerFlowConf.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyCloudBaseRunServerFlowConfRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyCloudBaseRunServerFlowConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudBaseRunServerFlowConf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudBaseRunServerFlowConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCloudBaseRunServerVersion(self, request):
        """修改服务版本的副本数，环境变量

        :param request: Request instance for ModifyCloudBaseRunServerVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyCloudBaseRunServerVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyCloudBaseRunServerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloudBaseRunServerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloudBaseRunServerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClsTopic(self, request):
        """修改日志主题

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDatabaseACL(self, request):
        """修改数据库权限

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEndUser(self, request):
        """管理终端用户

        :param request: Request instance for ModifyEndUser.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEndUserRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEndUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEndUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyEndUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEnv(self, request):
        """更新环境信息

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGatewayVersionTraffic(self, request):
        """设置网关版本的流量比例

        :param request: Request instance for ModifyGatewayVersionTraffic.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyGatewayVersionTrafficRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyGatewayVersionTrafficResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatewayVersionTraffic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatewayVersionTrafficResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReinstateEnv(self, request):
        """针对已隔离的免费环境，可以通过本接口将其恢复访问。

        :param request: Request instance for ReinstateEnv.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ReinstateEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ReinstateEnvResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReinstateEnv", params, headers=headers)
            response = json.loads(body)
            model = models.ReinstateEnvResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceActivityRecord(self, request):
        """更新活动详情

        :param request: Request instance for ReplaceActivityRecord.
        :type request: :class:`tencentcloud.tcb.v20180608.models.ReplaceActivityRecordRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ReplaceActivityRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceActivityRecord", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceActivityRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RollUpdateCloudBaseRunServerVersion(self, request):
        """针对特定的版本，进行滚动更新

        :param request: Request instance for RollUpdateCloudBaseRunServerVersion.
        :type request: :class:`tencentcloud.tcb.v20180608.models.RollUpdateCloudBaseRunServerVersionRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.RollUpdateCloudBaseRunServerVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollUpdateCloudBaseRunServerVersion", params, headers=headers)
            response = json.loads(body)
            model = models.RollUpdateCloudBaseRunServerVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SearchClsLog(self, request):
        """搜索CLS日志，TCB角色密钥访问

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
                raise TencentCloudSDKException(e.message, e.message)


    def TurnOffStandaloneGateway(self, request):
        """本接口（TurnOffStandaloneGateway）用于关闭小租户网关。

        :param request: Request instance for TurnOffStandaloneGateway.
        :type request: :class:`tencentcloud.tcb.v20180608.models.TurnOffStandaloneGatewayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.TurnOffStandaloneGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TurnOffStandaloneGateway", params, headers=headers)
            response = json.loads(body)
            model = models.TurnOffStandaloneGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TurnOnStandaloneGateway(self, request):
        """本接口（TurnOnStandaloneGateway）用于开启小租户网关。

        :param request: Request instance for TurnOnStandaloneGateway.
        :type request: :class:`tencentcloud.tcb.v20180608.models.TurnOnStandaloneGatewayRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.TurnOnStandaloneGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TurnOnStandaloneGateway", params, headers=headers)
            response = json.loads(body)
            model = models.TurnOnStandaloneGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnfreezeCloudBaseRunServers(self, request):
        """批量解冻服务

        :param request: Request instance for UnfreezeCloudBaseRunServers.
        :type request: :class:`tencentcloud.tcb.v20180608.models.UnfreezeCloudBaseRunServersRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.UnfreezeCloudBaseRunServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnfreezeCloudBaseRunServers", params, headers=headers)
            response = json.loads(body)
            model = models.UnfreezeCloudBaseRunServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)