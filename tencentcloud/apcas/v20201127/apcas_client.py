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
from tencentcloud.apcas.v20201127 import models


class ApcasClient(AbstractClient):
    _apiVersion = '2020-11-27'
    _endpoint = 'apcas.tencentcloudapi.com'
    _service = 'apcas'


    def GetTaskDetail(self, request):
        """查询画像洞察任务详情

        :param request: Request instance for GetTaskDetail.
        :type request: :class:`tencentcloud.apcas.v20201127.models.GetTaskDetailRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.GetTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTaskList(self, request):
        """查询当前账号AppID下的画像洞察任务列表

        :param request: Request instance for GetTaskList.
        :type request: :class:`tencentcloud.apcas.v20201127.models.GetTaskListRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.GetTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.GetTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PredictRating(self, request):
        """根据传入的设备号（IMEI、IDFA、手机号、手机号MD5），返回意向评级结果

        :param request: Request instance for PredictRating.
        :type request: :class:`tencentcloud.apcas.v20201127.models.PredictRatingRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.PredictRatingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PredictRating", params, headers=headers)
            response = json.loads(body)
            model = models.PredictRatingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCallDetails(self, request):
        """查询调用明细

        :param request: Request instance for QueryCallDetails.
        :type request: :class:`tencentcloud.apcas.v20201127.models.QueryCallDetailsRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.QueryCallDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCallDetails", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCallDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryCallStat(self, request):
        """按时间维度获取调用量统计

        :param request: Request instance for QueryCallStat.
        :type request: :class:`tencentcloud.apcas.v20201127.models.QueryCallStatRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.QueryCallStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryCallStat", params, headers=headers)
            response = json.loads(body)
            model = models.QueryCallStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryGeneralStat(self, request):
        """获取日/月/周/总调用量统计数据

        :param request: Request instance for QueryGeneralStat.
        :type request: :class:`tencentcloud.apcas.v20201127.models.QueryGeneralStatRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.QueryGeneralStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryGeneralStat", params, headers=headers)
            response = json.loads(body)
            model = models.QueryGeneralStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadId(self, request):
        """上传群体画像的ID列表（支持的ID类型：0:imei 7:IDFA 8:MD5(imei)），后台返回生成的画像分析任务ID

        :param request: Request instance for UploadId.
        :type request: :class:`tencentcloud.apcas.v20201127.models.UploadIdRequest`
        :rtype: :class:`tencentcloud.apcas.v20201127.models.UploadIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadId", params, headers=headers)
            response = json.loads(body)
            model = models.UploadIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))