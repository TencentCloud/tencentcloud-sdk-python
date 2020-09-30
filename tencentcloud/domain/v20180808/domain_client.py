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
from tencentcloud.domain.v20180808 import models


class DomainClient(AbstractClient):
    _apiVersion = '2018-08-08'
    _endpoint = 'domain.tencentcloudapi.com'


    def CheckBatchStatus(self, request):
        """本接口 ( CheckBatchStatus ) 用于检查批量任务状态 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for CheckBatchStatus.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckBatchStatusRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckBatchStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckBatchStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckBatchStatusResponse()
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


    def CheckDomain(self, request):
        """检查域名是否可以注册。

        :param request: Request instance for CheckDomain.
        :type request: :class:`tencentcloud.domain.v20180808.models.CheckDomainRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CheckDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckDomainResponse()
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


    def CreateDomainBatch(self, request):
        """本接口 ( CreateDomainBatch ) 用于批量注册域名 。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for CreateDomainBatch.
        :type request: :class:`tencentcloud.domain.v20180808.models.CreateDomainBatchRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.CreateDomainBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDomainBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainBatchResponse()
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


    def DescribeDomainBaseInfo(self, request):
        """本接口 (  DescribeDomainBaseInfo) 获取域名基础信息。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for DescribeDomainBaseInfo.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainBaseInfoRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainBaseInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainBaseInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainBaseInfoResponse()
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


    def DescribeDomainNameList(self, request):
        """本接口 (  DescribeDomainNameList ) 获取域名列表。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for DescribeDomainNameList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainNameListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainNameListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainNameList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainNameListResponse()
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


    def DescribeDomainPriceList(self, request):
        """按照域名后缀获取对应的价格列表

        :param request: Request instance for DescribeDomainPriceList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeDomainPriceListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeDomainPriceListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainPriceList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainPriceListResponse()
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


    def DescribeTemplateList(self, request):
        """本接口 (DescribeTemplateList) 用于获取模板列表。

        默认接口请求频率限制：20次/秒。

        :param request: Request instance for DescribeTemplateList.
        :type request: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateListRequest`
        :rtype: :class:`tencentcloud.domain.v20180808.models.DescribeTemplateListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTemplateList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplateListResponse()
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