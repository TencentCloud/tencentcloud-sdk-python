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
from tencentcloud.irp.v20220324 import models


class IrpClient(AbstractClient):
    _apiVersion = '2022-03-24'
    _endpoint = 'irp.tencentcloudapi.com'
    _service = 'irp'


    def RecommendContent(self, request):
        """获取推荐结果

        :param request: Request instance for RecommendContent.
        :type request: :class:`tencentcloud.irp.v20220324.models.RecommendContentRequest`
        :rtype: :class:`tencentcloud.irp.v20220324.models.RecommendContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecommendContent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecommendContentResponse()
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


    def ReportAction(self, request):
        """上报行为

        :param request: Request instance for ReportAction.
        :type request: :class:`tencentcloud.irp.v20220324.models.ReportActionRequest`
        :rtype: :class:`tencentcloud.irp.v20220324.models.ReportActionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportAction", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportActionResponse()
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


    def ReportMaterial(self, request):
        """上报物料

        :param request: Request instance for ReportMaterial.
        :type request: :class:`tencentcloud.irp.v20220324.models.ReportMaterialRequest`
        :rtype: :class:`tencentcloud.irp.v20220324.models.ReportMaterialResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportMaterial", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportMaterialResponse()
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


    def ReportPortrait(self, request):
        """上报用户画像

        :param request: Request instance for ReportPortrait.
        :type request: :class:`tencentcloud.irp.v20220324.models.ReportPortraitRequest`
        :rtype: :class:`tencentcloud.irp.v20220324.models.ReportPortraitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportPortrait", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportPortraitResponse()
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