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
from tencentcloud.bma.v20210624 import models


class BmaClient(AbstractClient):
    _apiVersion = '2021-06-24'
    _endpoint = 'bma.tencentcloudapi.com'
    _service = 'bma'


    def CreateCRBlock(self, request):
        """版权保护-新建拦截接口

        :param request: Request instance for CreateCRBlock.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRBlockRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRBlock", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCRBlockResponse()
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


    def CreateCRCompanyVerify(self, request):
        """品牌经营管家-版权保护模块企业认证接口

        :param request: Request instance for CreateCRCompanyVerify.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRCompanyVerifyRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRCompanyVerifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRCompanyVerify", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCRCompanyVerifyResponse()
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


    def CreateCRRight(self, request):
        """版权保护-新建发函接口

        :param request: Request instance for CreateCRRight.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRRightRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRRightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRRight", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCRRightResponse()
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


    def DescribeCRWorkInfo(self, request):
        """查询作品基本信息

        :param request: Request instance for DescribeCRWorkInfo.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeCRWorkInfoRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeCRWorkInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCRWorkInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCRWorkInfoResponse()
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