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
from tencentcloud.cr.v20180321 import models


class CrClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'cr.tencentcloudapi.com'


    def ApplyBlackList(self, request):
        """提交黑名单申请。

        :param request: 调用ApplyBlackList所需参数的结构体。
        :type request: :class:`tencentcloud.cr.v20180321.models.ApplyBlackListRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ApplyBlackListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyBlackList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyBlackListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRecords(self, request):
        """查询录音，返回录音列表。

        :param request: 调用DescribeRecords所需参数的结构体。
        :type request: :class:`tencentcloud.cr.v20180321.models.DescribeRecordsRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DescribeRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRecordsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskStatus(self, request):
        """客户调用该接口查看任务执行状态。输入任务ID，输出任务执行状态或者结果

        :param request: 调用DescribeTaskStatus所需参数的结构体。
        :type request: :class:`tencentcloud.cr.v20180321.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadReport(self, request):
        """客户调用该接口下载指定日期的催收报告

        :param request: 调用DownloadReport所需参数的结构体。
        :type request: :class:`tencentcloud.cr.v20180321.models.DownloadReportRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DownloadReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadReportResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadDataFile(self, request):
        """客户通过调用该接口上传需催收文档或还款文档，接口返回任务ID。

        :param request: 调用UploadDataFile所需参数的结构体。
        :type request: :class:`tencentcloud.cr.v20180321.models.UploadDataFileRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.UploadDataFileResponse`

        """
        try:
            params = request._serialize()
            options = {'IsMultipart': True, 'BinaryParams': [u'File']}
            body = self.call("UploadDataFile", params, options=options)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadDataFileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadFile(self, request):
        """客户通过调用该接口上传需催收文档，格式需为excel格式。接口返回任务ID。

        :param request: 调用UploadFile所需参数的结构体。
        :type request: :class:`tencentcloud.cr.v20180321.models.UploadFileRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.UploadFileResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadFile", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadFileResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)