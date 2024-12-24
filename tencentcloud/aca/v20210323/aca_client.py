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
from tencentcloud.aca.v20210323 import models


class AcaClient(AbstractClient):
    _apiVersion = '2021-03-23'
    _endpoint = 'aca.tencentcloudapi.com'
    _service = 'aca'


    def GetDrugIndications(self, request):
        """药品适应症接口

        :param request: Request instance for GetDrugIndications.
        :type request: :class:`tencentcloud.aca.v20210323.models.GetDrugIndicationsRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.GetDrugIndicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDrugIndications", params, headers=headers)
            response = json.loads(body)
            model = models.GetDrugIndicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LoginHisTool(self, request):
        """登录获取token

        :param request: Request instance for LoginHisTool.
        :type request: :class:`tencentcloud.aca.v20210323.models.LoginHisToolRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginHisToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginHisTool", params, headers=headers)
            response = json.loads(body)
            model = models.LoginHisToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LoginOutHisTool(self, request):
        """登出

        :param request: Request instance for LoginOutHisTool.
        :type request: :class:`tencentcloud.aca.v20210323.models.LoginOutHisToolRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.LoginOutHisToolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginOutHisTool", params, headers=headers)
            response = json.loads(body)
            model = models.LoginOutHisToolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SmartDrugInfo(self, request):
        """智能用药接口

        :param request: Request instance for SmartDrugInfo.
        :type request: :class:`tencentcloud.aca.v20210323.models.SmartDrugInfoRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.SmartDrugInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SmartDrugInfo", params, headers=headers)
            response = json.loads(body)
            model = models.SmartDrugInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SmartPredict(self, request):
        """辅诊智能预测接口

        :param request: Request instance for SmartPredict.
        :type request: :class:`tencentcloud.aca.v20210323.models.SmartPredictRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.SmartPredictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SmartPredict", params, headers=headers)
            response = json.loads(body)
            model = models.SmartPredictResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncDepartment(self, request):
        """用于院方科室管理，获取科室列表和状态、新增或修改科室信息、删除科室。

        :param request: Request instance for SyncDepartment.
        :type request: :class:`tencentcloud.aca.v20210323.models.SyncDepartmentRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.SyncDepartmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncDepartment", params, headers=headers)
            response = json.loads(body)
            model = models.SyncDepartmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncStandardDict(self, request):
        """同步标准字典，如给药频次、给药途径、科室、诊断等

        :param request: Request instance for SyncStandardDict.
        :type request: :class:`tencentcloud.aca.v20210323.models.SyncStandardDictRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.SyncStandardDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncStandardDict", params, headers=headers)
            response = json.loads(body)
            model = models.SyncStandardDictResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadDrugs(self, request):
        """药品同步，一次同步数据不要超过500个

        :param request: Request instance for UploadDrugs.
        :type request: :class:`tencentcloud.aca.v20210323.models.UploadDrugsRequest`
        :rtype: :class:`tencentcloud.aca.v20210323.models.UploadDrugsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadDrugs", params, headers=headers)
            response = json.loads(body)
            model = models.UploadDrugsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))