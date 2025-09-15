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