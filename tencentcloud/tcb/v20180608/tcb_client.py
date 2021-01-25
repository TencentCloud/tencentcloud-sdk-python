# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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


    def CheckTcbService(self, request):
        """检查是否开通Tcb服务

        :param request: Request instance for CheckTcbService.
        :type request: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.CheckTcbServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckTcbService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckTcbServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CommonServiceAPI", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CommonServiceAPIResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateAuthDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAuthDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateCloudBaseRunResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCloudBaseRunResourceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateCloudBaseRunServerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCloudBaseRunServerVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateHostingDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHostingDomainResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreatePostpayPackage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePostpayPackageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("CreateStaticStore", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStaticStoreResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteCloudBaseProjectLatestVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCloudBaseProjectLatestVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DeleteEndUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEndUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeAuthDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuthDomainsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeCloudBaseBuildService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudBaseBuildServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeCloudBaseRunResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudBaseRunResourceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeCloudBaseRunResourceForExtend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudBaseRunResourceForExtendResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeCloudBaseRunServerVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudBaseRunServerVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeCloudBaseRunVersionSnapshot", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudBaseRunVersionSnapshotResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeDatabaseACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseACLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeDownloadFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDownloadFileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeEndUserLoginStatistic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEndUserLoginStatisticResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeEndUserStatistic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEndUserStatisticResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeEndUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEndUsersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeEnvFreeQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvFreeQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeEnvLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvLimitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeEnvs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeExtraPkgBillingInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeExtraPkgBillingInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribePostpayFreeQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePostpayFreeQuotasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribePostpayPackageFreeQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePostpayPackageFreeQuotasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeQuotaData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQuotaDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DescribeSmsQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSmsQuotasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DestroyEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("DestroyStaticStore", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyStaticStoreResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("EstablishCloudBaseRunServer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EstablishCloudBaseRunServerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyDatabaseACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDatabaseACLResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyEndUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEndUserResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ModifyEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
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
            body = self.call("ReinstateEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReinstateEnvResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)