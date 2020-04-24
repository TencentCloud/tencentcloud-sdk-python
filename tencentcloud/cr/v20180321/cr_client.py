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
        """提交黑名单后，黑名单中有效期内的号码将停止拨打，适用于到期/逾期提醒、回访场景。

        :param request: Request instance for ApplyBlackList.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyCreditAudit(self, request):
        """提交信审外呼申请，返回当次请求日期。

        :param request: Request instance for ApplyCreditAudit.
        :type request: :class:`tencentcloud.cr.v20180321.models.ApplyCreditAuditRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ApplyCreditAuditResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyCreditAudit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyCreditAuditResponse()
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


    def DescribeCreditResult(self, request):
        """根据信审任务ID和请求日期，获取相关信审结果。

        :param request: Request instance for DescribeCreditResult.
        :type request: :class:`tencentcloud.cr.v20180321.models.DescribeCreditResultRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DescribeCreditResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCreditResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCreditResultResponse()
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


    def DescribeRecords(self, request):
        """用于获取指定案件的录音地址，次日早上8:00后可查询前日录音。

        :param request: Request instance for DescribeRecords.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskStatus(self, request):
        """根据上传文件接口的输出参数DataResId，获取相关上传结果。

        :param request: Request instance for DescribeTaskStatus.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadDialogueText(self, request):
        """用于获取指定案件的对话文本内容，次日早上8:00后可查询前日对话文本内容。

        :param request: Request instance for DownloadDialogueText.
        :type request: :class:`tencentcloud.cr.v20180321.models.DownloadDialogueTextRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DownloadDialogueTextResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadDialogueText", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadDialogueTextResponse()
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


    def DownloadRecordList(self, request):
        """<p>用于获取录音下载链接清单，次日早上8:00后可查询前日录音清单。</p>
        <p>注意：录音清单中的录音下载链接仅次日20:00之前有效，请及时下载。</p>

        :param request: Request instance for DownloadRecordList.
        :type request: :class:`tencentcloud.cr.v20180321.models.DownloadRecordListRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DownloadRecordListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadRecordList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadRecordListResponse()
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


    def DownloadReport(self, request):
        """用于下载结果报表。当日23:00后，可获取当日到期/逾期提醒结果，次日00:30后，可获取昨日回访结果。

        :param request: Request instance for DownloadReport.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryInstantData(self, request):
        """实时数据查询

        :param request: Request instance for QueryInstantData.
        :type request: :class:`tencentcloud.cr.v20180321.models.QueryInstantDataRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.QueryInstantDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryInstantData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryInstantDataResponse()
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


    def UploadDataFile(self, request):
        """上传文件，接口返回数据任务ID，支持xlsx、xls、csv、zip格式。

        :param request: Request instance for UploadDataFile.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadDataJson(self, request):
        """上传Json格式数据，接口返回数据任务ID

        :param request: Request instance for UploadDataJson.
        :type request: :class:`tencentcloud.cr.v20180321.models.UploadDataJsonRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.UploadDataJsonResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadDataJson", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadDataJsonResponse()
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


    def UploadFile(self, request):
        """客户通过调用该接口上传需催收文档，格式需为excel格式。接口返回任务ID。

        :param request: Request instance for UploadFile.
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)