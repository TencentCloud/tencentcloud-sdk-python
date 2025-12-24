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


    def BindEnvGateway(self, request):
        r"""绑定另外一个环境下的网关，callContainer请求可以访问到该网关

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


    def CommonServiceAPI(self, request):
        r"""TCB云API统一入口

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndDeployCloudBaseProject(self, request):
        r"""创建云开发项目

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuthDomain(self, request):
        r"""增加安全域名

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


    def CreateCloudBaseRunResource(self, request):
        r"""开通容器托管的资源，包括集群创建，VPC配置，异步任务创建，镜像托管，Coding等，查看创建结果需要根据DescribeCloudBaseRunResource接口来查看

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudBaseRunServerVersion(self, request):
        r"""创建服务版本

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


    def CreatePostpayPackage(self, request):
        r"""开通后付费资源

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


    def DeleteCloudBaseProjectLatestVersion(self, request):
        r"""删除云项目

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCloudBaseRunServerVersion(self, request):
        r"""删除服务版本

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGatewayVersion(self, request):
        r"""删除网关某版本

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWxGatewayRoute(self, request):
        r"""删除安全网关路由

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeActivityRecord(self, request):
        r"""查询活动记录信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuthDomains(self, request):
        r"""获取安全域名列表

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
        r"""获取计费相关信息

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


    def DescribeCbrServerVersion(self, request):
        r"""查询服务版本的详情

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


    def DescribeCloudBaseProjectLatestVersionList(self, request):
        r"""获取云开发项目列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseProjectVersionList(self, request):
        r"""云项目部署列表

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseRunResource(self, request):
        r"""查看容器托管的集群状态

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseRunResourceForExtend(self, request):
        r"""查看容器托管的集群状态扩展使用

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseRunServer(self, request):
        r"""查询单个服务的详情，版本以及详情

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


    def DescribeCloudBaseRunVersion(self, request):
        r"""查询服务版本详情(新)

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloudBaseRunVersionSnapshot(self, request):
        r"""查询版本历史

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCurveData(self, request):
        r"""根据用户传入的指标, 拉取一段时间内的监控数据。

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
        r"""获取数据库权限

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


    def DescribeDownloadFile(self, request):
        r"""获取下载文件信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvDealRegion(self, request):
        r"""获取环境下单地域

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnvFreeQuota(self, request):
        r"""查询后付费免费配额信息

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


    def DescribeEnvPostpaidDeduct(self, request):
        r"""查询环境后付费计费详情

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


    def DescribeExtensionUploadInfo(self, request):
        r"""描述扩展上传文件信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtraPkgBillingInfo(self, request):
        r"""获取增值包计费相关信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayCurveData(self, request):
        r"""查询网关监控数据

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


    def DescribeGraphData(self, request):
        r"""根据用户传入的指标, 拉取一段时间内的监控数据。

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


    def DescribePostpayFreeQuotas(self, request):
        r"""查询后付费资源免费量

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePostpayPackageFreeQuotas(self, request):
        r"""获取后付费免费额度

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


    def DescribeSmsQuotas(self, request):
        r"""查询后付费短信资源量
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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecialCostItems(self, request):
        r"""查询环境1分钱抵扣信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserActivityInfo(self, request):
        r"""查询用户活动信息

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWxGatewayRoutes(self, request):
        r"""查看安全网关路由

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWxGateways(self, request):
        r"""查看安全网关

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyEnv(self, request):
        r"""销毁环境

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


    def EditAuthConfig(self, request):
        r"""修改登录配置

        :param request: Request instance for EditAuthConfig.
        :type request: :class:`tencentcloud.tcb.v20180608.models.EditAuthConfigRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.EditAuthConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EditAuthConfig", params, headers=headers)
            response = json.loads(body)
            model = models.EditAuthConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EstablishCloudBaseRunServer(self, request):
        r"""创建云应用服务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EstablishWxGatewayRoute(self, request):
        r"""创建或修改安全网关路由

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FreezeCloudBaseRunServers(self, request):
        r"""批量冻结

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudBaseRunServerFlowConf(self, request):
        r"""修改容器内的版本流量配置

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloudBaseRunServerVersion(self, request):
        r"""修改服务版本的副本数，环境变量

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
        r"""修改数据库权限

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


    def ModifyGatewayVersionTraffic(self, request):
        r"""设置网关版本的流量比例

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReinstateEnv(self, request):
        r"""针对已隔离的免费环境，可以通过本接口将其恢复访问。

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceActivityRecord(self, request):
        r"""更新活动详情

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClsLog(self, request):
        r"""搜索CLS日志，TCB角色密钥访问

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


    def UnfreezeCloudBaseRunServers(self, request):
        r"""批量解冻服务

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
                raise TencentCloudSDKException(type(e).__name__, str(e))