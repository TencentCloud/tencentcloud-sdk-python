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


    def CreateBPFakeURL(self, request):
        """添加仿冒链接（举报）

        :param request: Request instance for CreateBPFakeURL.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateBPFakeURLRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateBPFakeURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPFakeURL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPFakeURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPFalseTicket(self, request):
        """添加误报工单

        :param request: Request instance for CreateBPFalseTicket.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateBPFalseTicketRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateBPFalseTicketResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPFalseTicket", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPFalseTicketResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPOfflineAttachment(self, request):
        """添加下线材料

        :param request: Request instance for CreateBPOfflineAttachment.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateBPOfflineAttachmentRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateBPOfflineAttachmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPOfflineAttachment", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPOfflineAttachmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPOfflineTicket(self, request):
        """添加下线工单

        :param request: Request instance for CreateBPOfflineTicket.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateBPOfflineTicketRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateBPOfflineTicketResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPOfflineTicket", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPOfflineTicketResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBPProtectURLs(self, request):
        """添加保护网站

        :param request: Request instance for CreateBPProtectURLs.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateBPProtectURLsRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateBPProtectURLsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBPProtectURLs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBPProtectURLsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRBlock(self, request):
        """新建协查处置

        :param request: Request instance for CreateCRBlock.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRBlockRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRBlock", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRCompanyVerify(self, request):
        """本接口用于企业认证，新接入用户必须认证后才可以进行后续操作（个人认证和企业认证二选一），只需认证一次即可

        :param request: Request instance for CreateCRCompanyVerify.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRCompanyVerifyRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRCompanyVerifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRCompanyVerify", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRCompanyVerifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRDesktopCode(self, request):
        """新建过程取证码

        :param request: Request instance for CreateCRDesktopCode.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRDesktopCodeRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRDesktopCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRDesktopCode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRDesktopCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRObtain(self, request):
        """版权保护-新建取证接口

        :param request: Request instance for CreateCRObtain.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRObtainRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRObtainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRObtain", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRObtainResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.CreateCRRightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRRightFile(self, request):
        """权属文件添加

        :param request: Request instance for CreateCRRightFile.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRRightFileRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRRightFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRRightFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRRightFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRTort(self, request):
        """举报侵权链接

        :param request: Request instance for CreateCRTort.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRTortRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRTortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRTort", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRTortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRUserVerify(self, request):
        """本接口用于个人认证，新接入用户必须认证后才可以进行后续操作（个人认证和企业认证二选一），只需认证一次即可

        :param request: Request instance for CreateCRUserVerify.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRUserVerifyRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRUserVerifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRUserVerify", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRUserVerifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCRWork(self, request):
        """新建作品

        :param request: Request instance for CreateCRWork.
        :type request: :class:`tencentcloud.bma.v20210624.models.CreateCRWorkRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.CreateCRWorkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCRWork", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCRWorkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBPCompanyInfo(self, request):
        """查询企业信息

        :param request: Request instance for DescribeBPCompanyInfo.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeBPCompanyInfoRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeBPCompanyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPCompanyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPCompanyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBPFakeURLs(self, request):
        """查询仿冒链接

        :param request: Request instance for DescribeBPFakeURLs.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeBPFakeURLsRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeBPFakeURLsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPFakeURLs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPFakeURLsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBPProtectURLs(self, request):
        """查询保护网站

        :param request: Request instance for DescribeBPProtectURLs.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeBPProtectURLsRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeBPProtectURLsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPProtectURLs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPProtectURLsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBPReportFakeURLs(self, request):
        """查询举报列表

        :param request: Request instance for DescribeBPReportFakeURLs.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeBPReportFakeURLsRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeBPReportFakeURLsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBPReportFakeURLs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBPReportFakeURLsResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeCRMonitorDetailResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeCRMonitorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCRObtainDetail(self, request):
        """查询取证详情

        :param request: Request instance for DescribeCRObtainDetail.
        :type request: :class:`tencentcloud.bma.v20210624.models.DescribeCRObtainDetailRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.DescribeCRObtainDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCRObtainDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCRObtainDetailResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.DescribeCRWorkInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBPOfflineAttachment(self, request):
        """修改下线材料

        :param request: Request instance for ModifyBPOfflineAttachment.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyBPOfflineAttachmentRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyBPOfflineAttachmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBPOfflineAttachment", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBPOfflineAttachmentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCRBlockStatus(self, request):
        """协查处置申请

        :param request: Request instance for ModifyCRBlockStatus.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRBlockStatusRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRBlockStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRBlockStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCRBlockStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCRMonitor(self, request):
        """开启/关闭监测

        :param request: Request instance for ModifyCRMonitor.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRMonitorRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCRMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCRObtainStatus(self, request):
        """取证申请

        :param request: Request instance for ModifyCRObtainStatus.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRObtainStatusRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRObtainStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRObtainStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCRObtainStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCRRightStatus(self, request):
        """发函申请

        :param request: Request instance for ModifyCRRightStatus.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRRightStatusRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRRightStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRRightStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCRRightStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCRWhiteList(self, request):
        """修改白名单列表

        :param request: Request instance for ModifyCRWhiteList.
        :type request: :class:`tencentcloud.bma.v20210624.models.ModifyCRWhiteListRequest`
        :rtype: :class:`tencentcloud.bma.v20210624.models.ModifyCRWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCRWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCRWhiteListResponse()
            model._deserialize(response["Response"])
            return model
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
            model = models.UpdateCRWorkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)