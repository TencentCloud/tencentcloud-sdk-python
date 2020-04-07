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
from tencentcloud.ssl.v20191205 import models


class SslClient(AbstractClient):
    _apiVersion = '2019-12-05'
    _endpoint = 'ssl.tencentcloudapi.com'


    def ApplyCertificate(self, request):
        """本接口（ApplyCertificate）用于免费证书申请。

        :param request: Request instance for ApplyCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ApplyCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ApplyCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyCertificateResponse()
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


    def CancelCertificateOrder(self, request):
        """取消证书订单。

        :param request: Request instance for CancelCertificateOrder.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CancelCertificateOrderRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CancelCertificateOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelCertificateOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelCertificateOrderResponse()
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


    def CommitCertificateInformation(self, request):
        """提交证书订单。

        :param request: Request instance for CommitCertificateInformation.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CommitCertificateInformationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CommitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CommitCertificateInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CommitCertificateInformationResponse()
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


    def DeleteCertificate(self, request):
        """本接口（DeleteCertificate）用于删除证书。

        :param request: Request instance for DeleteCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCertificateResponse()
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


    def DescribeCertificate(self, request):
        """本接口（DescribeCertificate）用于获取证书信息。

        :param request: Request instance for DescribeCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateResponse()
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


    def DescribeCertificateDetail(self, request):
        """获取证书详情。

        :param request: Request instance for DescribeCertificateDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificateDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateDetailResponse()
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


    def DescribeCertificateOperateLogs(self, request):
        """获取用户账号下有关证书的操作日志。

        :param request: Request instance for DescribeCertificateOperateLogs.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateOperateLogsRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateOperateLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificateOperateLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateOperateLogsResponse()
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


    def DescribeCertificates(self, request):
        """本接口（DescribeCertificates）用于获取证书列表。

        :param request: Request instance for DescribeCertificates.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificatesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificatesResponse()
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


    def DownloadCertificate(self, request):
        """本接口（DownloadCertificate）用于下载证书。

        :param request: Request instance for DownloadCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DownloadCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DownloadCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadCertificateResponse()
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


    def ModifyCertificateAlias(self, request):
        """用户传入证书id和备注来修改证书备注。

        :param request: Request instance for ModifyCertificateAlias.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateAliasRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateAliasResponse()
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


    def ModifyCertificateProject(self, request):
        """批量修改证书所属项目。

        :param request: Request instance for ModifyCertificateProject.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateProjectRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificateProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateProjectResponse()
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


    def ReplaceCertificate(self, request):
        """本接口（ReplaceCertificate）用于重颁发证书。已申请的免费证书仅支持 RSA 算法、密钥对参数为2048的证书重颁发，并且目前仅支持1次重颁发。

        :param request: Request instance for ReplaceCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ReplaceCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ReplaceCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceCertificateResponse()
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


    def SubmitCertificateInformation(self, request):
        """提交证书资料。

        :param request: Request instance for SubmitCertificateInformation.
        :type request: :class:`tencentcloud.ssl.v20191205.models.SubmitCertificateInformationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SubmitCertificateInformation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitCertificateInformationResponse()
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


    def UploadCertificate(self, request):
        """本接口（UploadCertificate）用于上传证书。

        :param request: Request instance for UploadCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadCertificateResponse()
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