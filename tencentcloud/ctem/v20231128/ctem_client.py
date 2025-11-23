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
from tencentcloud.ctem.v20231128 import models


class CtemClient(AbstractClient):
    _apiVersion = '2023-11-28'
    _endpoint = 'ctem.tencentcloudapi.com'
    _service = 'ctem'


    def CreateApp(self, request):
        r"""添加APP资产

        :param request: Request instance for CreateApp.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateAppRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAsset(self, request):
        r"""添加主机资产

        :param request: Request instance for CreateAsset.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateAssetRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAsset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomer(self, request):
        r"""创建企业

        :param request: Request instance for CreateCustomer.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateCustomerRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateCustomerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDomain(self, request):
        r"""添加主域名数据

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateEnterprise(self, request):
        r"""添加企业架构资产

        :param request: Request instance for CreateEnterprise.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateEnterpriseRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateEnterpriseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnterprise", params, headers=headers)
            response = json.loads(body)
            model = models.CreateEnterpriseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHttp(self, request):
        r"""添加网站资产

        :param request: Request instance for CreateHttp.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateHttpRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateHttpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHttp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHttpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateJobRecord(self, request):
        r"""启动测绘

        :param request: Request instance for CreateJobRecord.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateJobRecordRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateJobRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJobRecord", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJobRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateManage(self, request):
        r"""添加后台数据

        :param request: Request instance for CreateManage.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateManageRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateManageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateManage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateManageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePort(self, request):
        r"""添加端口服务资产

        :param request: Request instance for CreatePort.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreatePortRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreatePortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePort", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSeeds(self, request):
        r"""创建种子

        :param request: Request instance for CreateSeeds.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateSeedsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateSeedsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSeeds", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSeedsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubDomain(self, request):
        r"""添加子域名数据

        :param request: Request instance for CreateSubDomain.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateSubDomainRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateSubDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubDomain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSuspiciousAsset(self, request):
        r"""添加影子资产

        :param request: Request instance for CreateSuspiciousAsset.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateSuspiciousAssetRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateSuspiciousAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSuspiciousAsset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSuspiciousAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWechatApplet(self, request):
        r"""添加微信小程序资产

        :param request: Request instance for CreateWechatApplet.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateWechatAppletRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateWechatAppletResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWechatApplet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWechatAppletResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWechatOfficialAccount(self, request):
        r"""添加微信公众号资产

        :param request: Request instance for CreateWechatOfficialAccount.
        :type request: :class:`tencentcloud.ctem.v20231128.models.CreateWechatOfficialAccountRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.CreateWechatOfficialAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWechatOfficialAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWechatOfficialAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteApps(self, request):
        r"""删除APP数据

        :param request: Request instance for DeleteApps.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteAppsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApps", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssets(self, request):
        r"""删除主机资产数据

        :param request: Request instance for DeleteAssets.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteAssetsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDomains(self, request):
        r"""删除主域名数据

        :param request: Request instance for DeleteDomains.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteDomainsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteEnterprises(self, request):
        r"""删除企业架构数据

        :param request: Request instance for DeleteEnterprises.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteEnterprisesRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteEnterprisesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEnterprises", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteEnterprisesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHttps(self, request):
        r"""删除网站资产数据

        :param request: Request instance for DeleteHttps.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteHttpsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteHttpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHttps", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHttpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteManages(self, request):
        r"""删除后台数据

        :param request: Request instance for DeleteManages.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteManagesRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteManagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteManages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteManagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePorts(self, request):
        r"""删除端口数据

        :param request: Request instance for DeletePorts.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeletePortsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeletePortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePorts", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSeeds(self, request):
        r"""删除种子

        :param request: Request instance for DeleteSeeds.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteSeedsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteSeedsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSeeds", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSeedsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubDomains(self, request):
        r"""删除子域名数据

        :param request: Request instance for DeleteSubDomains.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteSubDomainsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteSubDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSuspiciousAssets(self, request):
        r"""删除影子资产数据

        :param request: Request instance for DeleteSuspiciousAssets.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteSuspiciousAssetsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteSuspiciousAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSuspiciousAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSuspiciousAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWechatApplets(self, request):
        r"""删除微信小程序数据

        :param request: Request instance for DeleteWechatApplets.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteWechatAppletsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteWechatAppletsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWechatApplets", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWechatAppletsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWechatOfficialAccounts(self, request):
        r"""删除微信公众号数据

        :param request: Request instance for DeleteWechatOfficialAccounts.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DeleteWechatOfficialAccountsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DeleteWechatOfficialAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWechatOfficialAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWechatOfficialAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApiSecs(self, request):
        r"""查看API安全数据

        :param request: Request instance for DescribeApiSecs.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeApiSecsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeApiSecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApiSecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApiSecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApps(self, request):
        r"""查看移动端资产

        :param request: Request instance for DescribeApps.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeAppsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssets(self, request):
        r"""查看主机资产

        :param request: Request instance for DescribeAssets.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeAssetsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConfigs(self, request):
        r"""查看目录爆破数据

        :param request: Request instance for DescribeConfigs.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeConfigsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomers(self, request):
        r"""查看企业列表

        :param request: Request instance for DescribeCustomers.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeCustomersRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeCustomersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDarkWebs(self, request):
        r"""查看暗网数据

        :param request: Request instance for DescribeDarkWebs.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeDarkWebsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeDarkWebsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDarkWebs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDarkWebsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        r"""查看主域名数据

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEnterprises(self, request):
        r"""查看企业架构数据

        :param request: Request instance for DescribeEnterprises.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeEnterprisesRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeEnterprisesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnterprises", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEnterprisesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFakeApps(self, request):
        r"""查询仿冒应用

        :param request: Request instance for DescribeFakeApps.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeAppsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeAppsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFakeApps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFakeAppsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFakeMiniPrograms(self, request):
        r"""查询仿冒小程序

        :param request: Request instance for DescribeFakeMiniPrograms.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeMiniProgramsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeMiniProgramsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFakeMiniPrograms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFakeMiniProgramsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFakeWebsites(self, request):
        r"""查询仿冒网站

        :param request: Request instance for DescribeFakeWebsites.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeWebsitesRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeWebsitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFakeWebsites", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFakeWebsitesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFakeWechatOfficials(self, request):
        r"""查询仿冒公众号

        :param request: Request instance for DescribeFakeWechatOfficials.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeWechatOfficialsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeFakeWechatOfficialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFakeWechatOfficials", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFakeWechatOfficialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGithubs(self, request):
        r"""查看Github泄露数据

        :param request: Request instance for DescribeGithubs.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeGithubsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeGithubsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGithubs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGithubsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHttps(self, request):
        r"""查看http数据

        :param request: Request instance for DescribeHttps.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeHttpsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeHttpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHttps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHttpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobRecordDetails(self, request):
        r"""查看链路详情

        :param request: Request instance for DescribeJobRecordDetails.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeJobRecordDetailsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeJobRecordDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobRecordDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobRecordDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobRecords(self, request):
        r"""查看任务运行记录列表

        :param request: Request instance for DescribeJobRecords.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeJobRecordsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeJobRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLeakageCodes(self, request):
        r"""获取代码泄露数据

        :param request: Request instance for DescribeLeakageCodes.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeLeakageCodesRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeLeakageCodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLeakageCodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLeakageCodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLeakageDatas(self, request):
        r"""获取数据泄露事件

        :param request: Request instance for DescribeLeakageDatas.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeLeakageDatasRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeLeakageDatasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLeakageDatas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLeakageDatasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLeakageEmails(self, request):
        r"""获取邮箱泄露数据

        :param request: Request instance for DescribeLeakageEmails.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeLeakageEmailsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeLeakageEmailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLeakageEmails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLeakageEmailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeManages(self, request):
        r"""查看后台管理数据

        :param request: Request instance for DescribeManages.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeManagesRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeManagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeManages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeManagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetDisks(self, request):
        r"""查看网盘泄露数据

        :param request: Request instance for DescribeNetDisks.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeNetDisksRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeNetDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePorts(self, request):
        r"""查看端口数据

        :param request: Request instance for DescribePorts.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribePortsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribePortsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePorts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSeeds(self, request):
        r"""查看种子列表

        :param request: Request instance for DescribeSeeds.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeSeedsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeSeedsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSeeds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSeedsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSensitiveInfos(self, request):
        r"""查看敏感信息泄露数据

        :param request: Request instance for DescribeSensitiveInfos.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeSensitiveInfosRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeSensitiveInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSensitiveInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSensitiveInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubDomains(self, request):
        r"""查看子域名数据

        :param request: Request instance for DescribeSubDomains.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeSubDomainsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeSubDomainsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubDomains", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubDomainsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSuspiciousAssets(self, request):
        r"""查看影子资产

        :param request: Request instance for DescribeSuspiciousAssets.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeSuspiciousAssetsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeSuspiciousAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSuspiciousAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSuspiciousAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVuls(self, request):
        r"""查看漏洞数据

        :param request: Request instance for DescribeVuls.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeVulsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVuls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVulsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWeakPasswords(self, request):
        r"""查看弱口令数据

        :param request: Request instance for DescribeWeakPasswords.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeWeakPasswordsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeWeakPasswordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWeakPasswords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWeakPasswordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWechatApplets(self, request):
        r"""查看微信小程序

        :param request: Request instance for DescribeWechatApplets.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeWechatAppletsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeWechatAppletsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWechatApplets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWechatAppletsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWechatOfficialAccounts(self, request):
        r"""查看公众号数据

        :param request: Request instance for DescribeWechatOfficialAccounts.
        :type request: :class:`tencentcloud.ctem.v20231128.models.DescribeWechatOfficialAccountsRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.DescribeWechatOfficialAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWechatOfficialAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWechatOfficialAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IgnoreData(self, request):
        r"""忽略数据

        :param request: Request instance for IgnoreData.
        :type request: :class:`tencentcloud.ctem.v20231128.models.IgnoreDataRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.IgnoreDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IgnoreData", params, headers=headers)
            response = json.loads(body)
            model = models.IgnoreDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomer(self, request):
        r"""编辑企业

        :param request: Request instance for ModifyCustomer.
        :type request: :class:`tencentcloud.ctem.v20231128.models.ModifyCustomerRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.ModifyCustomerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLabel(self, request):
        r"""修改标签

        :param request: Request instance for ModifyLabel.
        :type request: :class:`tencentcloud.ctem.v20231128.models.ModifyLabelRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.ModifyLabelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLabel", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLabelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySeedStatus(self, request):
        r"""修改种子状态

        :param request: Request instance for ModifySeedStatus.
        :type request: :class:`tencentcloud.ctem.v20231128.models.ModifySeedStatusRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.ModifySeedStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySeedStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySeedStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopJobRecord(self, request):
        r"""停止扫描

        :param request: Request instance for StopJobRecord.
        :type request: :class:`tencentcloud.ctem.v20231128.models.StopJobRecordRequest`
        :rtype: :class:`tencentcloud.ctem.v20231128.models.StopJobRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopJobRecord", params, headers=headers)
            response = json.loads(body)
            model = models.StopJobRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))