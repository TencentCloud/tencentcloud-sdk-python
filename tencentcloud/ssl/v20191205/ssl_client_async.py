# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ssl.v20191205 import models
from typing import Dict


class SslClient(AbstractClient):
    _apiVersion = '2019-12-05'
    _endpoint = 'ssl.tencentcloudapi.com'
    _service = 'ssl'

    async def ApplyCertificate(
            self,
            request: models.ApplyCertificateRequest,
            opts: Dict = None,
    ) -> models.ApplyCertificateResponse:
        """
        本接口（ApplyCertificate）用于免费证书申请。
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelAuditCertificate(
            self,
            request: models.CancelAuditCertificateRequest,
            opts: Dict = None,
    ) -> models.CancelAuditCertificateResponse:
        """
        取消证书审核
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAuditCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAuditCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelCertificateOrder(
            self,
            request: models.CancelCertificateOrderRequest,
            opts: Dict = None,
    ) -> models.CancelCertificateOrderResponse:
        """
        取消证书订单。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelCertificateOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelCertificateOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CertificateInfoSubmit(
            self,
            request: models.CertificateInfoSubmitRequest,
            opts: Dict = None,
    ) -> models.CertificateInfoSubmitResponse:
        """
        付费提交证书资料
        """
        
        kwargs = {}
        kwargs["action"] = "CertificateInfoSubmit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CertificateInfoSubmitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CertificateOrderSubmit(
            self,
            request: models.CertificateOrderSubmitRequest,
            opts: Dict = None,
    ) -> models.CertificateOrderSubmitResponse:
        """
        提交付费证书订单
        """
        
        kwargs = {}
        kwargs["action"] = "CertificateOrderSubmit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CertificateOrderSubmitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCertificateChain(
            self,
            request: models.CheckCertificateChainRequest,
            opts: Dict = None,
    ) -> models.CheckCertificateChainResponse:
        """
        本接口（CheckCertificateChain）用于检查证书链是否完整。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCertificateChain"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCertificateChainResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCertificateDomainVerification(
            self,
            request: models.CheckCertificateDomainVerificationRequest,
            opts: Dict = None,
    ) -> models.CheckCertificateDomainVerificationResponse:
        """
        检查证书域名验证结果
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCertificateDomainVerification"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCertificateDomainVerificationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCertificateExist(
            self,
            request: models.CheckCertificateExistRequest,
            opts: Dict = None,
    ) -> models.CheckCertificateExistResponse:
        """
        根据证书内容检测当前账号下是否存在一致的证书， 存在则返回证书ID， 不存在则返回空
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCertificateExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCertificateExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitCertificateInformation(
            self,
            request: models.CommitCertificateInformationRequest,
            opts: Dict = None,
    ) -> models.CommitCertificateInformationResponse:
        """
        付费证书提交订单； 本接口不维护新功能， 可使用新接口进行提交， [CertificateOrderSubmit](https://cloud.tencent.com/document/product/400/116032)
        """
        
        kwargs = {}
        kwargs["action"] = "CommitCertificateInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitCertificateInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompleteCertificate(
            self,
            request: models.CompleteCertificateRequest,
            opts: Dict = None,
    ) -> models.CompleteCertificateResponse:
        """
        本接口（CompleteCertificate）用于主动触发证书验证。DNSPod和Wotrus品牌的证书不支持使用此接口。
        """
        
        kwargs = {}
        kwargs["action"] = "CompleteCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompleteCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificate(
            self,
            request: models.CreateCertificateRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateResponse:
        """
        本接口（CreateCertificate）用于创建付费证书。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificateBindResourceSyncTask(
            self,
            request: models.CreateCertificateBindResourceSyncTaskRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateBindResourceSyncTaskResponse:
        """
        创建证书绑定关联云资源异步任务， 该接口用于查询证书关联云资源。 若证书ID已存在查询云资源任务，则结果返回该任务ID。关联云资源类型，支持以下云资源：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）、cos。查询关联云资源结果使用DescribeCertificateBindResourceTaskResult接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificateBindResourceSyncTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateBindResourceSyncTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCertificateByPackage(
            self,
            request: models.CreateCertificateByPackageRequest,
            opts: Dict = None,
    ) -> models.CreateCertificateByPackageResponse:
        """
        使用权益点创建证书
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCertificateByPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCertificateByPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCertificate(
            self,
            request: models.DeleteCertificateRequest,
            opts: Dict = None,
    ) -> models.DeleteCertificateResponse:
        """
        本接口（DeleteCertificate）用于删除证书。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCertificates(
            self,
            request: models.DeleteCertificatesRequest,
            opts: Dict = None,
    ) -> models.DeleteCertificatesResponse:
        """
        批量删除证书，删除证书前支持查询证书是否关联了腾讯云云资源 （需自定义配置参数，参数名称：IsSync）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteManager(
            self,
            request: models.DeleteManagerRequest,
            opts: Dict = None,
    ) -> models.DeleteManagerResponse:
        """
        删除管理人
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployCertificateInstance(
            self,
            request: models.DeployCertificateInstanceRequest,
            opts: Dict = None,
    ) -> models.DeployCertificateInstanceResponse:
        """
        证书部署到云资源实例列表，本接口只会创建部署任务， 部署任务结果可通过DescribeHostDeployRecordDetail查询。本接口创建部署任务时，会校验证书和部署实例的匹配关系，存在不匹配的则会创建部署任务失败。以下为匹配关系校验规则：
        - 若待部署的证书和传入实例域名的当前绑定的证书一致， 则不会创建成功
        - 若待部署的证书和传入域名不匹配， 则不会创建成功
        - 若部署clb实例时， 7层监听器下无规则，则不会创建成功
        - 若部署clb实例时， 7层监听器未开启SNI，该监听器下存在任一域名和证书不匹配， 则不会创建成功
        - 若部署clb实例时，监听器规则为正则表示式， 则不会创建成功

        <dx-alert infotype="explain" title="">一个证书ID，相同的资源类型，只能创建一个部署任务，必须等部署任务执行完成，才能创建新的部署任务</dx-alert>
        """
        
        kwargs = {}
        kwargs["action"] = "DeployCertificateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployCertificateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployCertificateRecordRetry(
            self,
            request: models.DeployCertificateRecordRetryRequest,
            opts: Dict = None,
    ) -> models.DeployCertificateRecordRetryResponse:
        """
        云资源部署重试部署记录
        """
        
        kwargs = {}
        kwargs["action"] = "DeployCertificateRecordRetry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployCertificateRecordRetryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployCertificateRecordRollback(
            self,
            request: models.DeployCertificateRecordRollbackRequest,
            opts: Dict = None,
    ) -> models.DeployCertificateRecordRollbackResponse:
        """
        云资源部署成功记录回滚， 部署失败的记录不会回滚； 接口调用成功后， 会创建一个用于回滚的部署任务， 并返回该任务的ID
        """
        
        kwargs = {}
        kwargs["action"] = "DeployCertificateRecordRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployCertificateRecordRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificate(
            self,
            request: models.DescribeCertificateRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateResponse:
        """
        本接口（DescribeCertificate）用于获取证书信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateBindResourceTaskDetail(
            self,
            request: models.DescribeCertificateBindResourceTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateBindResourceTaskDetailResponse:
        """
        查询CreateCertificateBindResourceSyncTask任务结果， 返回证书关联云资源异步任务结果， 支持以下云资源：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）、cos
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateBindResourceTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateBindResourceTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateBindResourceTaskResult(
            self,
            request: models.DescribeCertificateBindResourceTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateBindResourceTaskResultResponse:
        """
        查询CreateCertificateBindResourceSyncTask任务结果， 返回证书关联云资源异步任务结果， 支持以下云资源：clb、cdn、waf、live、vod、ddos、tke、apigateway、tcb、teo（edgeOne）、cos
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateBindResourceTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateBindResourceTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateDetail(
            self,
            request: models.DescribeCertificateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateDetailResponse:
        """
        获取证书详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificateOperateLogs(
            self,
            request: models.DescribeCertificateOperateLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificateOperateLogsResponse:
        """
        获取用户账号下有关证书的操作日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificateOperateLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificateOperateLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertificates(
            self,
            request: models.DescribeCertificatesRequest,
            opts: Dict = None,
    ) -> models.DescribeCertificatesResponse:
        """
        本接口（DescribeCertificates）用于获取证书列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertificates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertificatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCompanies(
            self,
            request: models.DescribeCompaniesRequest,
            opts: Dict = None,
    ) -> models.DescribeCompaniesResponse:
        """
        查询公司列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCompanies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCompaniesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeleteCertificatesTaskResult(
            self,
            request: models.DescribeDeleteCertificatesTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeDeleteCertificatesTaskResultResponse:
        """
        查询批量删除任务结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeleteCertificatesTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeleteCertificatesTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDeployedResources(
            self,
            request: models.DescribeDeployedResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeDeployedResourcesResponse:
        """
        证书查询关联资源， 最新查询接口请使用CreateCertificateBindResourceSyncTask， 可以查询更多支持的云资源
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDeployedResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDeployedResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDownloadCertificateUrl(
            self,
            request: models.DescribeDownloadCertificateUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeDownloadCertificateUrlResponse:
        """
        获取下载证书链接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDownloadCertificateUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDownloadCertificateUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostApiGatewayInstanceList(
            self,
            request: models.DescribeHostApiGatewayInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostApiGatewayInstanceListResponse:
        """
        查询证书apiGateway云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostApiGatewayInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostApiGatewayInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostCdnInstanceList(
            self,
            request: models.DescribeHostCdnInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostCdnInstanceListResponse:
        """
        查询证书cdn云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostCdnInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostCdnInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostClbInstanceList(
            self,
            request: models.DescribeHostClbInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostClbInstanceListResponse:
        """
        查询证书clb云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostClbInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostClbInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostCosInstanceList(
            self,
            request: models.DescribeHostCosInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostCosInstanceListResponse:
        """
        查询证书cos云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostCosInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostCosInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostDdosInstanceList(
            self,
            request: models.DescribeHostDdosInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostDdosInstanceListResponse:
        """
        查询证书ddos云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostDdosInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostDdosInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostDeployRecord(
            self,
            request: models.DescribeHostDeployRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeHostDeployRecordResponse:
        """
        查询证书云资源部署记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostDeployRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostDeployRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostDeployRecordDetail(
            self,
            request: models.DescribeHostDeployRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeHostDeployRecordDetailResponse:
        """
        查询证书云资源部署记录详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostDeployRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostDeployRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostLighthouseInstanceList(
            self,
            request: models.DescribeHostLighthouseInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostLighthouseInstanceListResponse:
        """
        查询证书Lighthouse云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostLighthouseInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostLighthouseInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostLiveInstanceList(
            self,
            request: models.DescribeHostLiveInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostLiveInstanceListResponse:
        """
        查询证书live云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostLiveInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostLiveInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostTeoInstanceList(
            self,
            request: models.DescribeHostTeoInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostTeoInstanceListResponse:
        """
        查询证书EdgeOne云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostTeoInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostTeoInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostTkeInstanceList(
            self,
            request: models.DescribeHostTkeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostTkeInstanceListResponse:
        """
        查询证书tke云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostTkeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostTkeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUpdateRecord(
            self,
            request: models.DescribeHostUpdateRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUpdateRecordResponse:
        """
        查询证书云资源更新记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUpdateRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUpdateRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUpdateRecordDetail(
            self,
            request: models.DescribeHostUpdateRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUpdateRecordDetailResponse:
        """
        查询证书云资源更新记录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUpdateRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUpdateRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUploadUpdateRecord(
            self,
            request: models.DescribeHostUploadUpdateRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUploadUpdateRecordResponse:
        """
        查询证书云资源更新（证书ID不变）记录列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUploadUpdateRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUploadUpdateRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostUploadUpdateRecordDetail(
            self,
            request: models.DescribeHostUploadUpdateRecordDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeHostUploadUpdateRecordDetailResponse:
        """
        查询证书更新（证书ID不变）部署记录详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostUploadUpdateRecordDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostUploadUpdateRecordDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostVodInstanceList(
            self,
            request: models.DescribeHostVodInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostVodInstanceListResponse:
        """
        查询证书Vod云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostVodInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostVodInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostWafInstanceList(
            self,
            request: models.DescribeHostWafInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostWafInstanceListResponse:
        """
        查询证书waf云资源部署实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostWafInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostWafInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeManagerDetail(
            self,
            request: models.DescribeManagerDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeManagerDetailResponse:
        """
        查询管理人详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeManagerDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeManagerDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeManagers(
            self,
            request: models.DescribeManagersRequest,
            opts: Dict = None,
    ) -> models.DescribeManagersResponse:
        """
        查询管理人列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeManagers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeManagersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackages(
            self,
            request: models.DescribePackagesRequest,
            opts: Dict = None,
    ) -> models.DescribePackagesResponse:
        """
        获得权益包列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadCertificate(
            self,
            request: models.DownloadCertificateRequest,
            opts: Dict = None,
    ) -> models.DownloadCertificateResponse:
        """
        本接口（DownloadCertificate）用于下载证书。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateAlias(
            self,
            request: models.ModifyCertificateAliasRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateAliasResponse:
        """
        用户传入证书id和备注来修改证书备注。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateProject(
            self,
            request: models.ModifyCertificateProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateProjectResponse:
        """
        批量修改证书所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificateResubmit(
            self,
            request: models.ModifyCertificateResubmitRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificateResubmitResponse:
        """
        针对审核失败或审核取消的付费证书，重新发起审核
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificateResubmit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificateResubmitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCertificatesExpiringNotificationSwitch(
            self,
            request: models.ModifyCertificatesExpiringNotificationSwitchRequest,
            opts: Dict = None,
    ) -> models.ModifyCertificatesExpiringNotificationSwitchResponse:
        """
        修改忽略证书到期通知。打开或关闭证书到期通知。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCertificatesExpiringNotificationSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCertificatesExpiringNotificationSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceCertificate(
            self,
            request: models.ReplaceCertificateRequest,
            opts: Dict = None,
    ) -> models.ReplaceCertificateResponse:
        """
        本接口（ReplaceCertificate）用于重颁发证书。已申请的免费证书仅支持 RSA 算法、密钥对参数为2048的证书重颁发，并且目前仅支持1次重颁发。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeCertificate(
            self,
            request: models.RevokeCertificateRequest,
            opts: Dict = None,
    ) -> models.RevokeCertificateResponse:
        """
        本接口（RevokeCertificate）用于吊销证书。
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitAuditManager(
            self,
            request: models.SubmitAuditManagerRequest,
            opts: Dict = None,
    ) -> models.SubmitAuditManagerResponse:
        """
        重新提交审核管理人
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitAuditManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitAuditManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitCertificateInformation(
            self,
            request: models.SubmitCertificateInformationRequest,
            opts: Dict = None,
    ) -> models.SubmitCertificateInformationResponse:
        """
        付费证书提交资料； 本接口不维护新功能， 可使用新接口进行资料提交， [CertificateInfoSubmit](https://cloud.tencent.com/document/product/400/116033)
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitCertificateInformation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitCertificateInformationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCertificateInstance(
            self,
            request: models.UpdateCertificateInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateCertificateInstanceResponse:
        """
        一键更新旧证书资源，本接口为异步接口， 调用之后DeployRecordId为0表示任务进行中， 重复请求这个接口， 当返回DeployRecordId大于0则表示任务创建成功。 未创建成功则会抛出异常
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCertificateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCertificateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCertificateRecordRetry(
            self,
            request: models.UpdateCertificateRecordRetryRequest,
            opts: Dict = None,
    ) -> models.UpdateCertificateRecordRetryResponse:
        """
        云资源更新重试部署记录
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCertificateRecordRetry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCertificateRecordRetryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCertificateRecordRollback(
            self,
            request: models.UpdateCertificateRecordRollbackRequest,
            opts: Dict = None,
    ) -> models.UpdateCertificateRecordRollbackResponse:
        """
        云资源更新成功记录回滚， 只对更新已成功的记录回滚
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCertificateRecordRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCertificateRecordRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadCertificate(
            self,
            request: models.UploadCertificateRequest,
            opts: Dict = None,
    ) -> models.UploadCertificateResponse:
        """
        本接口（UploadCertificate）用于上传证书。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadCertificate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadCertificateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadConfirmLetter(
            self,
            request: models.UploadConfirmLetterRequest,
            opts: Dict = None,
    ) -> models.UploadConfirmLetterResponse:
        """
        本接口（UploadConfirmLetter）上传证书确认函，不再维护其功能，请用户前往腾讯云证书控制台上传证书确认函
        """
        
        kwargs = {}
        kwargs["action"] = "UploadConfirmLetter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadConfirmLetterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadRevokeLetter(
            self,
            request: models.UploadRevokeLetterRequest,
            opts: Dict = None,
    ) -> models.UploadRevokeLetterResponse:
        """
        本接口（UploadRevokeLetter）上传证书吊销确认函，不再维护其功能，请用户前往腾讯云证书控制台上传证书吊销确认函
        """
        
        kwargs = {}
        kwargs["action"] = "UploadRevokeLetter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadRevokeLetterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadUpdateCertificateInstance(
            self,
            request: models.UploadUpdateCertificateInstanceRequest,
            opts: Dict = None,
    ) -> models.UploadUpdateCertificateInstanceResponse:
        """
        当前接口需联系加白使用并且只支持更新证书的CLB资源，更新证书内容（证书ID不变）并更新关联的云资源，本接口为异步接口， 调用之后DeployRecordId为0表示任务进行中， 重复请求这个接口， 当返回DeployRecordId大于0则表示任务创建成功。 未创建成功则会抛出异常
        """
        
        kwargs = {}
        kwargs["action"] = "UploadUpdateCertificateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadUpdateCertificateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadUpdateCertificateRecordRetry(
            self,
            request: models.UploadUpdateCertificateRecordRetryRequest,
            opts: Dict = None,
    ) -> models.UploadUpdateCertificateRecordRetryResponse:
        """
        云资源更新（证书ID不变）重试部署记录
        """
        
        kwargs = {}
        kwargs["action"] = "UploadUpdateCertificateRecordRetry"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadUpdateCertificateRecordRetryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadUpdateCertificateRecordRollback(
            self,
            request: models.UploadUpdateCertificateRecordRollbackRequest,
            opts: Dict = None,
    ) -> models.UploadUpdateCertificateRecordRollbackResponse:
        """
        云资源更新成功（证书ID不变）记录回滚， 会对全量任务进行回滚
        """
        
        kwargs = {}
        kwargs["action"] = "UploadUpdateCertificateRecordRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadUpdateCertificateRecordRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyManager(
            self,
            request: models.VerifyManagerRequest,
            opts: Dict = None,
    ) -> models.VerifyManagerResponse:
        """
        重新核验管理人
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)