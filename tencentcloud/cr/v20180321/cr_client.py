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
from tencentcloud.cr.v20180321 import models


class CrClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'cr.tencentcloudapi.com'
    _service = 'cr'


    def ApplyBlackList(self, request):
        """提交黑名单后，黑名单中有效期内的号码将停止拨打，适用于到期/逾期提醒、回访场景。

        :param request: Request instance for ApplyBlackList.
        :type request: :class:`tencentcloud.cr.v20180321.models.ApplyBlackListRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ApplyBlackListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyBlackList", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyBlackListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ApplyBlackListData(self, request):
        """提交机器人黑名单申请

        :param request: Request instance for ApplyBlackListData.
        :type request: :class:`tencentcloud.cr.v20180321.models.ApplyBlackListDataRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ApplyBlackListDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyBlackListData", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyBlackListDataResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ApplyCreditAudit", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyCreditAuditResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChangeBotCallStatus(self, request):
        """更新机器人任务作业状态

        :param request: Request instance for ChangeBotCallStatus.
        :type request: :class:`tencentcloud.cr.v20180321.models.ChangeBotCallStatusRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ChangeBotCallStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeBotCallStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeBotCallStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChangeBotTaskStatus(self, request):
        """更新机器人任务状态

        :param request: Request instance for ChangeBotTaskStatus.
        :type request: :class:`tencentcloud.cr.v20180321.models.ChangeBotTaskStatusRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ChangeBotTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeBotTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeBotTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBotTask(self, request):
        """创建机器人任务

        :param request: Request instance for CreateBotTask.
        :type request: :class:`tencentcloud.cr.v20180321.models.CreateBotTaskRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.CreateBotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBotTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBotFlow(self, request):
        """查询机器人对话流

        :param request: Request instance for DescribeBotFlow.
        :type request: :class:`tencentcloud.cr.v20180321.models.DescribeBotFlowRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DescribeBotFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBotFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBotFlowResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeCreditResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCreditResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFileModel(self, request):
        """查询机器人文件模板

        :param request: Request instance for DescribeFileModel.
        :type request: :class:`tencentcloud.cr.v20180321.models.DescribeFileModelRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DescribeFileModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileModel", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileModelResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecordsResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadBotRecord(self, request):
        """下载任务录音与文本，第二天12点后可使用此接口获取对应的录音与文本

        :param request: Request instance for DownloadBotRecord.
        :type request: :class:`tencentcloud.cr.v20180321.models.DownloadBotRecordRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.DownloadBotRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadBotRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadBotRecordResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DownloadDialogueText", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadDialogueTextResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DownloadRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadRecordListResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DownloadReport", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ExportBotData(self, request):
        """导出机器人数据

        :param request: Request instance for ExportBotData.
        :type request: :class:`tencentcloud.cr.v20180321.models.ExportBotDataRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.ExportBotDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportBotData", params, headers=headers)
            response = json.loads(body)
            model = models.ExportBotDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBlackListData(self, request):
        """查看黑名单数据列表

        :param request: Request instance for QueryBlackListData.
        :type request: :class:`tencentcloud.cr.v20180321.models.QueryBlackListDataRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.QueryBlackListDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBlackListData", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBlackListDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryBotList(self, request):
        """查询机器人任务状态列表

        :param request: Request instance for QueryBotList.
        :type request: :class:`tencentcloud.cr.v20180321.models.QueryBotListRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.QueryBotListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryBotList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryBotListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryCallList(self, request):
        """机器人任务查询

        :param request: Request instance for QueryCallList.
        :type request: :class:`tencentcloud.cr.v20180321.models.QueryCallListRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.QueryCallListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCallList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCallListResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("QueryInstantData", params, headers=headers)
            response = json.loads(body)
            model = models.QueryInstantDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryProducts(self, request):
        """查询产品列表

        :param request: Request instance for QueryProducts.
        :type request: :class:`tencentcloud.cr.v20180321.models.QueryProductsRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.QueryProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryProducts", params, headers=headers)
            response = json.loads(body)
            model = models.QueryProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryRecordList(self, request):
        """查询录音列表

        :param request: Request instance for QueryRecordList.
        :type request: :class:`tencentcloud.cr.v20180321.models.QueryRecordListRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.QueryRecordListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryRecordList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryRecordListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateBotTask(self, request):
        """更新机器人任务

        :param request: Request instance for UpdateBotTask.
        :type request: :class:`tencentcloud.cr.v20180321.models.UpdateBotTaskRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.UpdateBotTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBotTask", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBotTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadBotData(self, request):
        """上传机器人任务数据

        :param request: Request instance for UploadBotData.
        :type request: :class:`tencentcloud.cr.v20180321.models.UploadBotDataRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.UploadBotDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadBotData", params, headers=headers)
            response = json.loads(body)
            model = models.UploadBotDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadBotFile(self, request):
        """上传机器人文件

        :param request: Request instance for UploadBotFile.
        :type request: :class:`tencentcloud.cr.v20180321.models.UploadBotFileRequest`
        :rtype: :class:`tencentcloud.cr.v20180321.models.UploadBotFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadBotFile", params, headers=headers)
            response = json.loads(body)
            model = models.UploadBotFileResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("UploadDataFile", params, options=options, headers=headers)
            response = json.loads(body)
            model = models.UploadDataFileResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("UploadDataJson", params, headers=headers)
            response = json.loads(body)
            model = models.UploadDataJsonResponse()
            model._deserialize(response["Response"])
            return model
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
                raise TencentCloudSDKException(e.message, e.message)