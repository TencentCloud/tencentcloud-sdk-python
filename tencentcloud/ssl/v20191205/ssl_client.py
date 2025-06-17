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
from tencentcloud.ssl.v20191205 import models


class SslClient(AbstractClient):
    _apiVersion = '2019-12-05'
    _endpoint = 'ssl.tencentcloudapi.com'
    _service = 'ssl'


    def ApplyCertificate(self, request):
        """本接口（ApplyCertificate）用于免费证书申请。

        :param request: Request instance for ApplyCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ApplyCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ApplyCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelAuditCertificate(self, request):
        """取消证书审核

        :param request: Request instance for CancelAuditCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CancelAuditCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CancelAuditCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAuditCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAuditCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelCertificateOrder(self, request):
        """取消证书订单。

        :param request: Request instance for CancelCertificateOrder.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CancelCertificateOrderRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CancelCertificateOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelCertificateOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CancelCertificateOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CertificateInfoSubmit(self, request):
        """付费提交证书资料

        :param request: Request instance for CertificateInfoSubmit.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CertificateInfoSubmitRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateInfoSubmitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CertificateInfoSubmit", params, headers=headers)
            response = json.loads(body)
            model = models.CertificateInfoSubmitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CertificateOrderSubmit(self, request):
        """提交付费证书订单

        :param request: Request instance for CertificateOrderSubmit.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CertificateOrderSubmitRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CertificateOrderSubmitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CertificateOrderSubmit", params, headers=headers)
            response = json.loads(body)
            model = models.CertificateOrderSubmitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCertificateChain(self, request):
        """本接口（CheckCertificateChain）用于检查证书链是否完整。

        :param request: Request instance for CheckCertificateChain.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CheckCertificateChainRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CheckCertificateChainResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCertificateChain", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCertificateChainResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCertificateDomainVerification(self, request):
        """检查证书域名验证结果

        :param request: Request instance for CheckCertificateDomainVerification.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CheckCertificateDomainVerificationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CheckCertificateDomainVerificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCertificateDomainVerification", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCertificateDomainVerificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCertificateExist(self, request):
        """根据证书内容检测当前账号下是否存在一致的证书， 存在则返回证书ID， 不存在则返回空

        :param request: Request instance for CheckCertificateExist.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CheckCertificateExistRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CheckCertificateExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCertificateExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCertificateExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CommitCertificateInformation(self, request):
        """付费证书提交订单； 本接口不维护新功能， 可使用新接口进行提交， [CertificateOrderSubmit](https://cloud.tencent.com/document/product/400/116032)

        :param request: Request instance for CommitCertificateInformation.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CommitCertificateInformationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CommitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitCertificateInformation", params, headers=headers)
            response = json.loads(body)
            model = models.CommitCertificateInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteCertificate(self, request):
        """本接口（CompleteCertificate）用于主动触发证书验证。DNSPod和Wotrus品牌的证书不支持使用此接口。

        :param request: Request instance for CompleteCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CompleteCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CompleteCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCertificate(self, request):
        """本接口（CreateCertificate）用于创建付费证书。

        :param request: Request instance for CreateCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCertificateBindResourceSyncTask(self, request):
        """创建证书绑定关联云资源异步任务， 该接口用于查询证书关联云资源。 若证书ID已存在查询云资源任务，则结果返回该任务ID。关联云资源类型，支持以下云资源：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）、cos。查询关联云资源结果使用DescribeCertificateBindResourceTaskResult接口

        :param request: Request instance for CreateCertificateBindResourceSyncTask.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateBindResourceSyncTaskRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateBindResourceSyncTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCertificateBindResourceSyncTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCertificateBindResourceSyncTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCertificateByPackage(self, request):
        """使用权益点创建证书

        :param request: Request instance for CreateCertificateByPackage.
        :type request: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateByPackageRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.CreateCertificateByPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCertificateByPackage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCertificateByPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCertificate(self, request):
        """本接口（DeleteCertificate）用于删除证书。

        :param request: Request instance for DeleteCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCertificates(self, request):
        """批量删除证书，删除证书前支持查询证书是否关联了腾讯云云资源 （需自定义配置参数，参数名称：IsSync）

        :param request: Request instance for DeleteCertificates.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificatesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeleteCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteManager(self, request):
        """删除管理人

        :param request: Request instance for DeleteManager.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeleteManagerRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeleteManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteManager", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployCertificateInstance(self, request):
        """证书部署到云资源实例列表，本接口只会创建部署任务， 部署任务结果可通过DescribeHostDeployRecordDetail查询。本接口创建部署任务时，会校验证书和部署实例的匹配关系，存在不匹配的则会创建部署任务失败。以下为匹配关系校验规则：
        - 若待部署的证书和传入实例域名的当前绑定的证书一致， 则不会创建成功
        - 若待部署的证书和传入域名不匹配， 则不会创建成功
        - 若部署clb实例时， 7层监听器下无规则，则不会创建成功
        - 若部署clb实例时， 7层监听器未开启SNI，该监听器下存在任一域名和证书不匹配， 则不会创建成功
        - 若部署clb实例时，监听器规则为正则表示式， 则不会创建成功

        <dx-alert infotype="explain" title="">一个证书ID，相同的资源类型，只能创建一个部署任务，必须等部署任务执行完成，才能创建新的部署任务</dx-alert>

        :param request: Request instance for DeployCertificateInstance.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeployCertificateInstanceRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeployCertificateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployCertificateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeployCertificateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployCertificateRecordRetry(self, request):
        """云资源部署重试部署记录

        :param request: Request instance for DeployCertificateRecordRetry.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeployCertificateRecordRetryRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeployCertificateRecordRetryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployCertificateRecordRetry", params, headers=headers)
            response = json.loads(body)
            model = models.DeployCertificateRecordRetryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeployCertificateRecordRollback(self, request):
        """云资源部署成功记录回滚， 部署失败的记录不会回滚； 接口调用成功后， 会创建一个用于回滚的部署任务， 并返回该任务的ID

        :param request: Request instance for DeployCertificateRecordRollback.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DeployCertificateRecordRollbackRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DeployCertificateRecordRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployCertificateRecordRollback", params, headers=headers)
            response = json.loads(body)
            model = models.DeployCertificateRecordRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificate(self, request):
        """本接口（DescribeCertificate）用于获取证书信息。

        :param request: Request instance for DescribeCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateBindResourceTaskDetail(self, request):
        """查询CreateCertificateBindResourceSyncTask任务结果， 返回证书关联云资源异步任务结果， 支持以下云资源：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）、cos

        :param request: Request instance for DescribeCertificateBindResourceTaskDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateBindResourceTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateBindResourceTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateBindResourceTaskResult(self, request):
        """查询CreateCertificateBindResourceSyncTask任务结果， 返回证书关联云资源异步任务结果， 支持以下云资源：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）、cos

        :param request: Request instance for DescribeCertificateBindResourceTaskResult.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskResultRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateBindResourceTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateBindResourceTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateBindResourceTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateDetail(self, request):
        """获取证书详情。

        :param request: Request instance for DescribeCertificateDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificateOperateLogs(self, request):
        """获取用户账号下有关证书的操作日志。

        :param request: Request instance for DescribeCertificateOperateLogs.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateOperateLogsRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificateOperateLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificateOperateLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificateOperateLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCertificates(self, request):
        """本接口（DescribeCertificates）用于获取证书列表。

        :param request: Request instance for DescribeCertificates.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificatesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCertificates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCertificatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCompanies(self, request):
        """查询公司列表

        :param request: Request instance for DescribeCompanies.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeCompaniesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeCompaniesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCompanies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCompaniesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeleteCertificatesTaskResult(self, request):
        """查询批量删除任务结果

        :param request: Request instance for DescribeDeleteCertificatesTaskResult.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeDeleteCertificatesTaskResultRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeDeleteCertificatesTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeleteCertificatesTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeleteCertificatesTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeployedResources(self, request):
        """证书查询关联资源， 最新查询接口请使用CreateCertificateBindResourceSyncTask， 可以查询更多支持的云资源

        :param request: Request instance for DescribeDeployedResources.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeDeployedResourcesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeDeployedResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployedResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeployedResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDownloadCertificateUrl(self, request):
        """获取下载证书链接

        :param request: Request instance for DescribeDownloadCertificateUrl.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeDownloadCertificateUrlRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeDownloadCertificateUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDownloadCertificateUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDownloadCertificateUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostApiGatewayInstanceList(self, request):
        """查询证书apiGateway云资源部署实例列表

        :param request: Request instance for DescribeHostApiGatewayInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostApiGatewayInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostApiGatewayInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostApiGatewayInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostApiGatewayInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostCdnInstanceList(self, request):
        """查询证书cdn云资源部署实例列表

        :param request: Request instance for DescribeHostCdnInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostCdnInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostCdnInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostCdnInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostCdnInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostClbInstanceList(self, request):
        """查询证书clb云资源部署实例列表

        :param request: Request instance for DescribeHostClbInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostClbInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostClbInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostClbInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostClbInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostCosInstanceList(self, request):
        """查询证书cos云资源部署实例列表

        :param request: Request instance for DescribeHostCosInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostCosInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostCosInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostCosInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostCosInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostDdosInstanceList(self, request):
        """查询证书ddos云资源部署实例列表

        :param request: Request instance for DescribeHostDdosInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostDdosInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostDdosInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostDdosInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostDdosInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostDeployRecord(self, request):
        """查询证书云资源部署记录列表

        :param request: Request instance for DescribeHostDeployRecord.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostDeployRecordRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostDeployRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostDeployRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostDeployRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostDeployRecordDetail(self, request):
        """查询证书云资源部署记录详情列表

        :param request: Request instance for DescribeHostDeployRecordDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostDeployRecordDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostDeployRecordDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostDeployRecordDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostDeployRecordDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLighthouseInstanceList(self, request):
        """查询证书Lighthouse云资源部署实例列表

        :param request: Request instance for DescribeHostLighthouseInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostLighthouseInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostLighthouseInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLighthouseInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLighthouseInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostLiveInstanceList(self, request):
        """查询证书live云资源部署实例列表

        :param request: Request instance for DescribeHostLiveInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostLiveInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostLiveInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostLiveInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostLiveInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostTeoInstanceList(self, request):
        """查询证书EdgeOne云资源部署实例列表

        :param request: Request instance for DescribeHostTeoInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostTeoInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostTeoInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostTeoInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostTeoInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostTkeInstanceList(self, request):
        """查询证书tke云资源部署实例列表

        :param request: Request instance for DescribeHostTkeInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostTkeInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostTkeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostTkeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostTkeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostUpdateRecord(self, request):
        """查询证书云资源更新记录列表

        :param request: Request instance for DescribeHostUpdateRecord.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostUpdateRecord", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostUpdateRecordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostUpdateRecordDetail(self, request):
        """查询证书云资源更新记录详情

        :param request: Request instance for DescribeHostUpdateRecordDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostUpdateRecordDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostUpdateRecordDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostUpdateRecordDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostVodInstanceList(self, request):
        """查询证书Vod云资源部署实例列表

        :param request: Request instance for DescribeHostVodInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostVodInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostVodInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostVodInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostVodInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHostWafInstanceList(self, request):
        """查询证书waf云资源部署实例列表

        :param request: Request instance for DescribeHostWafInstanceList.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeHostWafInstanceListRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeHostWafInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHostWafInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHostWafInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeManagerDetail(self, request):
        """查询管理人详情

        :param request: Request instance for DescribeManagerDetail.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeManagerDetailRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeManagerDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeManagerDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeManagerDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeManagers(self, request):
        """查询管理人列表

        :param request: Request instance for DescribeManagers.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribeManagersRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribeManagersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeManagers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeManagersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePackages(self, request):
        """获得权益包列表

        :param request: Request instance for DescribePackages.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DescribePackagesRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DescribePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadCertificate(self, request):
        """本接口（DownloadCertificate）用于下载证书。

        :param request: Request instance for DownloadCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.DownloadCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.DownloadCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateAlias(self, request):
        """用户传入证书id和备注来修改证书备注。

        :param request: Request instance for ModifyCertificateAlias.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateAliasRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateProject(self, request):
        """批量修改证书所属项目。

        :param request: Request instance for ModifyCertificateProject.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateProjectRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificateResubmit(self, request):
        """针对审核失败或审核取消的付费证书，重新发起审核

        :param request: Request instance for ModifyCertificateResubmit.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateResubmitRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificateResubmitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificateResubmit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificateResubmitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCertificatesExpiringNotificationSwitch(self, request):
        """修改忽略证书到期通知。打开或关闭证书到期通知。

        :param request: Request instance for ModifyCertificatesExpiringNotificationSwitch.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificatesExpiringNotificationSwitchRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ModifyCertificatesExpiringNotificationSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCertificatesExpiringNotificationSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCertificatesExpiringNotificationSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceCertificate(self, request):
        """本接口（ReplaceCertificate）用于重颁发证书。已申请的免费证书仅支持 RSA 算法、密钥对参数为2048的证书重颁发，并且目前仅支持1次重颁发。

        :param request: Request instance for ReplaceCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.ReplaceCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.ReplaceCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeCertificate(self, request):
        """本接口（RevokeCertificate）用于吊销证书。

        :param request: Request instance for RevokeCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.RevokeCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.RevokeCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitAuditManager(self, request):
        """重新提交审核管理人

        :param request: Request instance for SubmitAuditManager.
        :type request: :class:`tencentcloud.ssl.v20191205.models.SubmitAuditManagerRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmitAuditManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitAuditManager", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitAuditManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitCertificateInformation(self, request):
        """付费证书提交资料； 本接口不维护新功能， 可使用新接口进行资料提交， [CertificateInfoSubmit](https://cloud.tencent.com/document/product/400/116033)

        :param request: Request instance for SubmitCertificateInformation.
        :type request: :class:`tencentcloud.ssl.v20191205.models.SubmitCertificateInformationRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.SubmitCertificateInformationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCertificateInformation", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCertificateInformationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCertificateInstance(self, request):
        """一键更新旧证书资源，本接口为异步接口， 调用之后DeployRecordId为0表示任务进行中， 重复请求这个接口， 当返回DeployRecordId大于0则表示任务创建成功。 未创建成功则会抛出异常

        :param request: Request instance for UpdateCertificateInstance.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateInstanceRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCertificateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCertificateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCertificateRecordRetry(self, request):
        """云资源更新重试部署记录

        :param request: Request instance for UpdateCertificateRecordRetry.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRetryRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRetryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCertificateRecordRetry", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCertificateRecordRetryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCertificateRecordRollback(self, request):
        """云资源更新成功记录回滚， 只对更新已成功的记录回滚

        :param request: Request instance for UpdateCertificateRecordRollback.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRollbackRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UpdateCertificateRecordRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCertificateRecordRollback", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCertificateRecordRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadCertificate(self, request):
        """本接口（UploadCertificate）用于上传证书。

        :param request: Request instance for UploadCertificate.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadCertificateRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadCertificateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadCertificate", params, headers=headers)
            response = json.loads(body)
            model = models.UploadCertificateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadConfirmLetter(self, request):
        """本接口（UploadConfirmLetter）上传证书确认函，不再维护其功能，请用户前往腾讯云证书控制台上传证书确认函

        :param request: Request instance for UploadConfirmLetter.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadConfirmLetterRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadConfirmLetterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadConfirmLetter", params, headers=headers)
            response = json.loads(body)
            model = models.UploadConfirmLetterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadRevokeLetter(self, request):
        """本接口（UploadRevokeLetter）上传证书吊销确认函，不再维护其功能，请用户前往腾讯云证书控制台上传证书吊销确认函

        :param request: Request instance for UploadRevokeLetter.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadRevokeLetterRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadRevokeLetterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadRevokeLetter", params, headers=headers)
            response = json.loads(body)
            model = models.UploadRevokeLetterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UploadUpdateCertificateInstance(self, request):
        """更新证书内容（证书ID不变）并更新关联的云资源，本接口为异步接口， 调用之后DeployRecordId为0表示任务进行中， 重复请求这个接口， 当返回DeployRecordId大于0则表示任务创建成功。 未创建成功则会抛出异常

        :param request: Request instance for UploadUpdateCertificateInstance.
        :type request: :class:`tencentcloud.ssl.v20191205.models.UploadUpdateCertificateInstanceRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.UploadUpdateCertificateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadUpdateCertificateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UploadUpdateCertificateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyManager(self, request):
        """重新核验管理人

        :param request: Request instance for VerifyManager.
        :type request: :class:`tencentcloud.ssl.v20191205.models.VerifyManagerRequest`
        :rtype: :class:`tencentcloud.ssl.v20191205.models.VerifyManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyManager", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))