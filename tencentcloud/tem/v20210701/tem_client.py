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
from tencentcloud.tem.v20210701 import models


class TemClient(AbstractClient):
    _apiVersion = '2021-07-01'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'


    def DescribeDeployApplicationDetail(self, request):
        """获取分批发布详情

        :param request: Request instance for DescribeDeployApplicationDetail.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeDeployApplicationDetailRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeDeployApplicationDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeployApplicationDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeployApplicationDetailResponse()
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


    def ResumeDeployApplication(self, request):
        """开始下一批次发布

        :param request: Request instance for ResumeDeployApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.ResumeDeployApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ResumeDeployApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResumeDeployApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeDeployApplicationResponse()
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


    def RevertDeployApplication(self, request):
        """回滚分批发布

        :param request: Request instance for RevertDeployApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.RevertDeployApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RevertDeployApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevertDeployApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevertDeployApplicationResponse()
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