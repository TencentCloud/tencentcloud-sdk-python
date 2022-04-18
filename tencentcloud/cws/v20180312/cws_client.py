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
from tencentcloud.cws.v20180312 import models


class CwsClient(AbstractClient):
    _apiVersion = '2018-03-12'
    _endpoint = 'cws.tencentcloudapi.com'
    _service = 'cws'


    def CreateMonitors(self, request):
        """本接口（CreateMonitors）用于新增一个或多个站点的监测任务。

        :param request: Request instance for CreateMonitors.
        :type request: :class:`tencentcloud.cws.v20180312.models.CreateMonitorsRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.CreateMonitorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMonitors", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMonitorsResponse()
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


    def CreateSites(self, request):
        """本接口（CreateSites）用于新增一个或多个站点。

        :param request: Request instance for CreateSites.
        :type request: :class:`tencentcloud.cws.v20180312.models.CreateSitesRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.CreateSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSites", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSitesResponse()
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


    def CreateSitesScans(self, request):
        """本接口（CreateSitesScans）用于新增一个或多个站点的单次扫描任务。

        :param request: Request instance for CreateSitesScans.
        :type request: :class:`tencentcloud.cws.v20180312.models.CreateSitesScansRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.CreateSitesScansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSitesScans", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSitesScansResponse()
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


    def CreateVulsMisinformation(self, request):
        """本接口（CreateVulsMisinformation）可以用于新增一个或多个漏洞误报信息。

        :param request: Request instance for CreateVulsMisinformation.
        :type request: :class:`tencentcloud.cws.v20180312.models.CreateVulsMisinformationRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.CreateVulsMisinformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulsMisinformation", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulsMisinformationResponse()
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


    def CreateVulsReport(self, request):
        """本接口 (CreateVulsReport) 用于生成漏洞报告并返回下载链接。

        :param request: Request instance for CreateVulsReport.
        :type request: :class:`tencentcloud.cws.v20180312.models.CreateVulsReportRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.CreateVulsReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVulsReport", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVulsReportResponse()
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


    def DeleteMonitors(self, request):
        """本接口 (DeleteMonitors) 用于删除用户监控任务。

        :param request: Request instance for DeleteMonitors.
        :type request: :class:`tencentcloud.cws.v20180312.models.DeleteMonitorsRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DeleteMonitorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMonitors", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMonitorsResponse()
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


    def DeleteSites(self, request):
        """本接口 (DeleteSites) 用于删除站点。

        :param request: Request instance for DeleteSites.
        :type request: :class:`tencentcloud.cws.v20180312.models.DeleteSitesRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DeleteSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSites", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSitesResponse()
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


    def DescribeConfig(self, request):
        """本接口 (DescribeConfig) 用于查询用户配置的详细信息。

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeMonitors(self, request):
        """本接口 (DescribeMonitors) 用于查询一个或多个监控任务的详细信息。

        :param request: Request instance for DescribeMonitors.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeMonitorsRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeMonitorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitors", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMonitorsResponse()
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


    def DescribeSiteQuota(self, request):
        """本接口 (DescribeSiteQuota) 用于查询用户购买的扫描次数总数和已使用数。

        :param request: Request instance for DescribeSiteQuota.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeSiteQuotaRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeSiteQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSiteQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSiteQuotaResponse()
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


    def DescribeSites(self, request):
        """本接口 (DescribeSites) 用于查询一个或多个站点的详细信息。

        :param request: Request instance for DescribeSites.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeSitesRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeSitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSites", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSitesResponse()
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


    def DescribeSitesVerification(self, request):
        """本接口 (DescribeSitesVerification) 用于查询一个或多个待验证站点的验证信息。

        :param request: Request instance for DescribeSitesVerification.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeSitesVerificationRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeSitesVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSitesVerification", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSitesVerificationResponse()
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


    def DescribeVuls(self, request):
        """本接口 (DescribeVuls) 用于查询一个或多个漏洞的详细信息。

        :param request: Request instance for DescribeVuls.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeVulsRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeVulsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVuls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsResponse()
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


    def DescribeVulsNumber(self, request):
        """本接口 (DescribeVulsNumber) 用于查询用户网站的漏洞总计数量。

        :param request: Request instance for DescribeVulsNumber.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeVulsNumberRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeVulsNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulsNumber", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsNumberResponse()
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


    def DescribeVulsNumberTimeline(self, request):
        """本接口 (DescribeVulsNumberTimeline) 用于查询漏洞数随时间变化统计信息。

        :param request: Request instance for DescribeVulsNumberTimeline.
        :type request: :class:`tencentcloud.cws.v20180312.models.DescribeVulsNumberTimelineRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.DescribeVulsNumberTimelineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVulsNumberTimeline", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVulsNumberTimelineResponse()
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


    def ModifyConfigAttribute(self, request):
        """本接口 (ModifyConfigAttribute) 用于修改用户配置的属性。

        :param request: Request instance for ModifyConfigAttribute.
        :type request: :class:`tencentcloud.cws.v20180312.models.ModifyConfigAttributeRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.ModifyConfigAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyConfigAttributeResponse()
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


    def ModifyMonitorAttribute(self, request):
        """本接口 (ModifyMonitorAttribute) 用于修改监测任务的属性。

        :param request: Request instance for ModifyMonitorAttribute.
        :type request: :class:`tencentcloud.cws.v20180312.models.ModifyMonitorAttributeRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.ModifyMonitorAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMonitorAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMonitorAttributeResponse()
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


    def ModifySiteAttribute(self, request):
        """本接口 (ModifySiteAttribute) 用于修改站点的属性。

        :param request: Request instance for ModifySiteAttribute.
        :type request: :class:`tencentcloud.cws.v20180312.models.ModifySiteAttributeRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.ModifySiteAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySiteAttribute", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySiteAttributeResponse()
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


    def VerifySites(self, request):
        """本接口 (VerifySites) 用于验证一个或多个待验证站点。

        :param request: Request instance for VerifySites.
        :type request: :class:`tencentcloud.cws.v20180312.models.VerifySitesRequest`
        :rtype: :class:`tencentcloud.cws.v20180312.models.VerifySitesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifySites", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifySitesResponse()
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