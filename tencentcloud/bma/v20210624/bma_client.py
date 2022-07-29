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


    def CreateCRWork(self, request):
        """版权保护-添加作品接口

        :param request: Request instance for CreateCRWork.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRWorkRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRWorkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRWork", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCRWorkResponse()
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


    def DescribeCRMonitorDetail(self, request):
        """版权保护-查询作品监测详情接口

        :param request: Request instance for DescribeCRMonitorDetail.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeCRMonitorDetailRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeCRMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCRMonitorDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCRMonitorDetailResponse()
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


    def DescribeCRMonitors(self, request):
        """版权保护-查询监测列表接口

        :param request: Request instance for DescribeCRMonitors.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeCRMonitorsRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeCRMonitorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCRMonitors", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCRMonitorsResponse()
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


    def ModifyCRBlockStatus(self, request):
        """版权保护-拦截申请接口

        :param request: Request instance for ModifyCRBlockStatus.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRBlockStatusRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRBlockStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRBlockStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCRBlockStatusResponse()
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


    def ModifyCRMonitor(self, request):
        """版权保护-修改监测状态接口

        :param request: Request instance for ModifyCRMonitor.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRMonitorRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRMonitor", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCRMonitorResponse()
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


    def ModifyCRObtainStatus(self, request):
        """申请取证

        :param request: Request instance for ModifyCRObtainStatus.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRObtainStatusRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRObtainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRObtainStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCRObtainStatusResponse()
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


    def ModifyCRRightStatus(self, request):
        """版权保护-维权申请接口

        :param request: Request instance for ModifyCRRightStatus.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRRightStatusRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRRightStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRRightStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCRRightStatusResponse()
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


    def UpdateCRWork(self, request):
        """更新作品

        :param request: Request instance for UpdateCRWork.
        :type request: :class:`tencentcloud.bma.v20210624.models.UpdateCRWorkRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.UpdateCRWorkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCRWork", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateCRWorkResponse()
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