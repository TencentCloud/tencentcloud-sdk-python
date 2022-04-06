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
from tencentcloud.bsca.v20210811 import models


class BscaClient(AbstractClient):
    _apiVersion = '2021-08-11'
    _endpoint = 'bsca.tencentcloudapi.com'
    _service = 'bsca'


    def DescribeKBComponent(self, request):
        """本接口(DescribeKBComponent)用于在知识库中查询开源组件信息。本接口根据用户输入的PURL在知识库中寻找对应的开源组件，其中Name为必填字段。

        :param request: Request instance for DescribeKBComponent.
        :type request: :class:`tencentcloud.bsca.v20210811.models.DescribeKBComponentRequest`
        :rtype: :class:`tencentcloud.bsca.v20210811.models.DescribeKBComponentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKBComponent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKBComponentResponse()
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


    def DescribeKBComponentVulnerability(self, request):
        """本接口(DescribeKBComponentVulnerability)用于在知识库中查询开源组件的漏洞信息。

        :param request: Request instance for DescribeKBComponentVulnerability.
        :type request: :class:`tencentcloud.bsca.v20210811.models.DescribeKBComponentVulnerabilityRequest`
        :rtype: :class:`tencentcloud.bsca.v20210811.models.DescribeKBComponentVulnerabilityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKBComponentVulnerability", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKBComponentVulnerabilityResponse()
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


    def DescribeKBLicense(self, request):
        """本接口(DescribeKBLicense)用于在知识库中查询许可证信息。

        :param request: Request instance for DescribeKBLicense.
        :type request: :class:`tencentcloud.bsca.v20210811.models.DescribeKBLicenseRequest`
        :rtype: :class:`tencentcloud.bsca.v20210811.models.DescribeKBLicenseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKBLicense", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKBLicenseResponse()
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


    def DescribeKBVulnerability(self, request):
        """本接口(DescribeKBVulnerability)用于在知识库中查询漏洞详细信息，支持根据CVE ID查询或者根据Vul ID查询。

        :param request: Request instance for DescribeKBVulnerability.
        :type request: :class:`tencentcloud.bsca.v20210811.models.DescribeKBVulnerabilityRequest`
        :rtype: :class:`tencentcloud.bsca.v20210811.models.DescribeKBVulnerabilityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKBVulnerability", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKBVulnerabilityResponse()
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