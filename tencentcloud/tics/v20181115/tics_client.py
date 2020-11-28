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
from tencentcloud.tics.v20181115 import models


class TicsClient(AbstractClient):
    _apiVersion = '2018-11-15'
    _endpoint = 'tics.tencentcloudapi.com'
    _service = 'tics'


    def DescribeDomainInfo(self, request):
        """提供域名相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。

        :param request: Request instance for DescribeDomainInfo.
        :type request: :class:`tencentcloud.tics.v20181115.models.DescribeDomainInfoRequest`
        :rtype: :class:`tencentcloud.tics.v20181115.models.DescribeDomainInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDomainInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDomainInfoResponse()
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


    def DescribeFileInfo(self, request):
        """提供文件相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。

        :param request: Request instance for DescribeFileInfo.
        :type request: :class:`tencentcloud.tics.v20181115.models.DescribeFileInfoRequest`
        :rtype: :class:`tencentcloud.tics.v20181115.models.DescribeFileInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileInfoResponse()
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


    def DescribeIpInfo(self, request):
        """提供IP相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。

        :param request: Request instance for DescribeIpInfo.
        :type request: :class:`tencentcloud.tics.v20181115.models.DescribeIpInfoRequest`
        :rtype: :class:`tencentcloud.tics.v20181115.models.DescribeIpInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpInfoResponse()
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


    def DescribeThreatInfo(self, request):
        """提供IP和域名相关威胁情报信息查询，这些信息可以辅助检测失陷主机、帮助SIEM/SOC等系统做研判决策、帮助运营团队对设备报警的编排处理。

        :param request: Request instance for DescribeThreatInfo.
        :type request: :class:`tencentcloud.tics.v20181115.models.DescribeThreatInfoRequest`
        :rtype: :class:`tencentcloud.tics.v20181115.models.DescribeThreatInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeThreatInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeThreatInfoResponse()
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