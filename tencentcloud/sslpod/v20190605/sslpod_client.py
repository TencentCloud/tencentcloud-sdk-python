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
from tencentcloud.sslpod.v20190605 import models


class SslpodClient(AbstractClient):
    _apiVersion = '2019-06-05'
    _endpoint = 'sslpod.tencentcloudapi.com'
    _service = 'sslpod'


    def CreateDomain(self, request):
        """通过域名端口添加监控

        :param request: Request instance for CreateDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainResponse()
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


    def DeleteDomain(self, request):
        """通过域名ID删除监控的域名

        :param request: Request instance for DeleteDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDomainResponse()
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


    def DescribeDashboard(self, request):
        """获取仪表盘数据

        :param request: Request instance for DescribeDashboard.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDashboardRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDashboardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDashboard", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDashboardResponse()
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


    def DescribeDomainCerts(self, request):
        """获取域名关联证书

        :param request: Request instance for DescribeDomainCerts.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainCertsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainCertsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainCerts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainCertsResponse()
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


    def DescribeDomainTags(self, request):
        """获取账号下所有tag

        :param request: Request instance for DescribeDomainTags.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainTagsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainTagsResponse()
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


    def DescribeDomains(self, request):
        """通过searchType搜索已经添加的域名

        :param request: Request instance for DescribeDomains.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainsResponse()
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


    def DescribeNoticeInfo(self, request):
        """获取通知额度信息

        :param request: Request instance for DescribeNoticeInfo.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.DescribeNoticeInfoRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.DescribeNoticeInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNoticeInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNoticeInfoResponse()
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


    def ModifyDomainTags(self, request):
        """修改域名tag

        :param request: Request instance for ModifyDomainTags.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.ModifyDomainTagsRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.ModifyDomainTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomainTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainTagsResponse()
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


    def RefreshDomain(self, request):
        """强制重新检测域名

        :param request: Request instance for RefreshDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.RefreshDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.RefreshDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RefreshDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefreshDomainResponse()
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


    def ResolveDomain(self, request):
        """解析域名获得多个IP地址

        :param request: Request instance for ResolveDomain.
        :type request: :class:`tencentcloud.sslpod.v20190605.models.ResolveDomainRequest`
        :rtype: :class:`tencentcloud.sslpod.v20190605.models.ResolveDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResolveDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResolveDomainResponse()
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