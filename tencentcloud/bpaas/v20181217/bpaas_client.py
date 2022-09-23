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
from tencentcloud.bpaas.v20181217 import models


class BpaasClient(AbstractClient):
    _apiVersion = '2018-12-17'
    _endpoint = 'bpaas.tencentcloudapi.com'
    _service = 'bpaas'


    def GetBpaasApproveDetail(self, request):
        """查看审批详情

        :param request: Request instance for GetBpaasApproveDetail.
        :type request: :class:`tencentcloud.bpaas.v20181217.models.GetBpaasApproveDetailRequest`
        :rtype: :class:`tencentcloud.bpaas.v20181217.models.GetBpaasApproveDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBpaasApproveDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBpaasApproveDetailResponse()
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


    def OutApproveBpaasApplication(self, request):
        """外部审批申请单

        :param request: Request instance for OutApproveBpaasApplication.
        :type request: :class:`tencentcloud.bpaas.v20181217.models.OutApproveBpaasApplicationRequest`
        :rtype: :class:`tencentcloud.bpaas.v20181217.models.OutApproveBpaasApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OutApproveBpaasApplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OutApproveBpaasApplicationResponse()
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