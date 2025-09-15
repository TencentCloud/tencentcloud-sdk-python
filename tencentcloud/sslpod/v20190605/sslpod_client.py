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
from tencentcloud.sslpod.v20190605 import models


class SslpodClient(AbstractClient):
    _apiVersion = '2019-06-05'
    _endpoint = 'sslpod.tencentcloudapi.com'
    _service = 'sslpod'


    def CreateDomain(self, request):
        r"""通过域名端口添加监控

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.CreateDomainResponse`

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


    def DeleteDomain(self, request):
        r"""通过域名ID删除监控的域名

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDomain", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDashboard(self, request):
        r"""获取仪表盘数据

        :param request: Request instance for DescribeDashboard.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDashboardRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainCerts(self, request):
        r"""获取域名关联证书

        :param request: Request instance for DescribeDomainCerts.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainCertsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainCertsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainCerts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainCertsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomainTags(self, request):
        r"""获取账号下所有tag

        :param request: Request instance for DescribeDomainTags.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainTagsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDomainTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDomainTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDomains(self, request):
        r"""通过searchType搜索已经添加的域名

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainsResponse`

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


    def DescribeNoticeInfo(self, request):
        r"""获取通知额度信息

        :param request: Request instance for DescribeNoticeInfo.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeNoticeInfoRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeNoticeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNoticeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNoticeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDomainTags(self, request):
        r"""修改域名tag

        :param request: Request instance for ModifyDomainTags.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.ModifyDomainTagsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.ModifyDomainTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDomainTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDomainTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshDomain(self, request):
        r"""强制重新检测域名

        :param request: Request instance for RefreshDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.RefreshDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.RefreshDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshDomain", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResolveDomain(self, request):
        r"""解析域名获得多个IP地址

        :param request: Request instance for ResolveDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.ResolveDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.ResolveDomainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResolveDomain", params, headers=headers)
            response = json.loads(body)
            model = models.ResolveDomainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))