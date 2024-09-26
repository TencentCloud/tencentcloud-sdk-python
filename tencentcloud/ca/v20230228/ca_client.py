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
from tencentcloud.ca.v20230228 import models


class CaClient(AbstractClient):
    _apiVersion = '2023-02-28'
    _endpoint = 'ca.tencentcloudapi.com'
    _service = 'ca'


    def CreateVerifyReport(self, request):
        """创建签名验证报告任务，此接口为异步盖章接口，盖章时效24小时。

        :param request: Request instance for CreateVerifyReport.
        :type request: :class:`tencentcloud.ca.v20230228.models.CreateVerifyReportRequest`
        :rtype: :class:`tencentcloud.ca.v20230228.models.CreateVerifyReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVerifyReport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVerifyReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVerifyReport(self, request):
        """下载验签报告url，url有效期默认12小时

        :param request: Request instance for DescribeVerifyReport.
        :type request: :class:`tencentcloud.ca.v20230228.models.DescribeVerifyReportRequest`
        :rtype: :class:`tencentcloud.ca.v20230228.models.DescribeVerifyReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVerifyReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVerifyReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadFile(self, request):
        """文件上传接口

        :param request: Request instance for UploadFile.
        :type request: :class:`tencentcloud.ca.v20230228.models.UploadFileRequest`
        :rtype: :class:`tencentcloud.ca.v20230228.models.UploadFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFile", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))