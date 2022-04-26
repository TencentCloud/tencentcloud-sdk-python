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
from tencentcloud.essbasic.v20210526 import models


class EssbasicClient(AbstractClient):
    _apiVersion = '2021-05-26'
    _endpoint = 'essbasic.tencentcloudapi.com'
    _service = 'essbasic'


    def ChannelCreateFlowByFiles(self, request):
        """接口（ChannelCreateFlowByFiles）用于渠道版通过文件创建流程。此接口不可直接使用，需要运营申请

        :param request: Request instance for ChannelCreateFlowByFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowByFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowByFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowByFiles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChannelCreateFlowByFilesResponse()
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


    def CreateConsoleLoginUrl(self, request):
        """此接口（CreateConsoleLoginUrl）用于创建电子签控制台登录链接。若企业未激活，调用同步企业信息、同步经办人信息

        :param request: Request instance for CreateConsoleLoginUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsoleLoginUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateConsoleLoginUrlResponse()
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


    def CreateFlowsByTemplates(self, request):
        """接口（CreateFlowsByTemplates）用于使用多个模板批量创建流程。当前可批量发起合同（流程）数量最大为20个。

        :param request: Request instance for CreateFlowsByTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowsByTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlowsByTemplatesResponse()
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


    def CreateSealByImage(self, request):
        """渠道通过图片为子客代创建印章，图片最大5m；此接口不可直接使用，需要运营申请

        :param request: Request instance for CreateSealByImage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSealByImageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSealByImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSealByImage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSealByImageResponse()
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


    def CreateSignUrls(self, request):
        """创建参与者签署短链

        :param request: Request instance for CreateSignUrls.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignUrls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSignUrlsResponse()
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


    def DescribeFlowDetailInfo(self, request):
        """此接口（DescribeFlowDetailInfo）用于查询合同(流程)的详细信息。

        :param request: Request instance for DescribeFlowDetailInfo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowDetailInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowDetailInfoResponse()
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


    def DescribeResourceUrlsByFlows(self, request):
        """根据流程信息批量获取资源下载链接

        :param request: Request instance for DescribeResourceUrlsByFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUrlsByFlows", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceUrlsByFlowsResponse()
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


    def DescribeTemplates(self, request):
        """通过此接口（DescribeTemplates）查询该企业在电子签渠道版中配置的有效模板列表

        :param request: Request instance for DescribeTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplatesResponse()
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


    def DescribeUsage(self, request):
        """此接口（DescribeUsage）用于获取渠道所有合作企业流量消耗情况。
         注: 此接口每日限频2次，若要扩大限制次数,请提前与客服经理或邮件至e-contract@tencent.com进行联系。

        :param request: Request instance for DescribeUsage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsageResponse()
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


    def GetDownloadFlowUrl(self, request):
        """此接口（GetDownloadFlowUrl）用于创建电子签批量下载地址，支持客户合同（流程）按照自定义文件夹形式 分类下载。
        当前接口限制最多合同（流程）50个.

        :param request: Request instance for GetDownloadFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDownloadFlowUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDownloadFlowUrlResponse()
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


    def OperateChannelTemplate(self, request):
        """此接口（OperateChannelTemplate）用于渠道侧将模板库中的模板对合作企业进行查询和设置, 其中包括可见性的修改以及对合作企业的设置.
        1、同步标识=select时：
        返回渠道侧模板库当前模板的属性.
        2、同步标识=update或者delete时：
        对渠道子客进行模板库中模板授权,修改操作

        :param request: Request instance for OperateChannelTemplate.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateChannelTemplate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OperateChannelTemplateResponse()
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


    def PrepareFlows(self, request):
        """该接口 (PrepareFlows) 用于创建待发起文件
        用户通过该接口进入流程发起的确认页面，进行发起信息二次确认， 如果确认则进行正常发起。
        目前该接口只支持B2C。

        :param request: Request instance for PrepareFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PrepareFlows", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PrepareFlowsResponse()
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


    def SyncProxyOrganization(self, request):
        """此接口（SyncProxyOrganization）用于同步渠道侧企业信息

        :param request: Request instance for SyncProxyOrganization.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncProxyOrganization", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncProxyOrganizationResponse()
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


    def SyncProxyOrganizationOperators(self, request):
        """此接口（SyncProxyOrganizationOperators）用于同步渠道合作企业经办人列表

        :param request: Request instance for SyncProxyOrganizationOperators.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncProxyOrganizationOperators", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncProxyOrganizationOperatorsResponse()
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


    def UploadFiles(self, request):
        """此接口（UploadFiles）用于文件上传。
        调用时需要设置Domain 为 file.ess.tencent.cn

        :param request: Request instance for UploadFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.UploadFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.UploadFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFiles", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadFilesResponse()
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