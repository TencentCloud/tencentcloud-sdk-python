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
from tencentcloud.ssm.v20190923 import models
from typing import Dict


class SsmClient(AbstractClient):
    _apiVersion = '2019-09-23'
    _endpoint = 'ssm.tencentcloudapi.com'
    _service = 'ssm'

    async def CreateProductSecret(
            self,
            request: models.CreateProductSecretRequest,
            opts: Dict = None,
    ) -> models.CreateProductSecretResponse:
        """
        创建云产品凭据
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProductSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProductSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSSHKeyPairSecret(
            self,
            request: models.CreateSSHKeyPairSecretRequest,
            opts: Dict = None,
    ) -> models.CreateSSHKeyPairSecretResponse:
        """
        创建用于托管SSH密钥对的凭据
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSSHKeyPairSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSSHKeyPairSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecret(
            self,
            request: models.CreateSecretRequest,
            opts: Dict = None,
    ) -> models.CreateSecretResponse:
        """
        创建新的凭据信息，通过KMS进行加密保护。每个Region最多可创建存储1000个凭据信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecret(
            self,
            request: models.DeleteSecretRequest,
            opts: Dict = None,
    ) -> models.DeleteSecretResponse:
        """
        删除指定的凭据信息，可以通过RecoveryWindowInDays参数设置立即删除或者计划删除。对于计划删除的凭据，在删除日期到达之前状态为 PendingDelete，并可以通过RestoreSecret 进行恢复，超出指定删除日期之后会被彻底删除。您必须先通过 DisableSecret 停用凭据后才可以进行（计划）删除操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecretVersion(
            self,
            request: models.DeleteSecretVersionRequest,
            opts: Dict = None,
    ) -> models.DeleteSecretVersionResponse:
        """
        该接口用于直接删除指定凭据下的单个版本凭据，删除操作立即生效，对所有状态下的凭据版本都可以删除。
        本接口仅适用于用户自定义凭据，本接口不能对云产品凭据进行操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecretVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecretVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAsyncRequestInfo(
            self,
            request: models.DescribeAsyncRequestInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAsyncRequestInfoResponse:
        """
        查询异步任务的执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAsyncRequestInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAsyncRequestInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRotationDetail(
            self,
            request: models.DescribeRotationDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRotationDetailResponse:
        """
        查询凭据轮转策略详情。
        本接口只适用于云产品凭据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRotationDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRotationDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRotationHistory(
            self,
            request: models.DescribeRotationHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeRotationHistoryResponse:
        """
        查询凭据轮转历史版本。
        本接口仅适用于云产品凭据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRotationHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRotationHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecret(
            self,
            request: models.DescribeSecretRequest,
            opts: Dict = None,
    ) -> models.DescribeSecretResponse:
        """
        获取凭据的详细属性信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSupportedProducts(
            self,
            request: models.DescribeSupportedProductsRequest,
            opts: Dict = None,
    ) -> models.DescribeSupportedProductsResponse:
        """
        查询支持的云产品列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSupportedProducts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSupportedProductsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableSecret(
            self,
            request: models.DisableSecretRequest,
            opts: Dict = None,
    ) -> models.DisableSecretResponse:
        """
        停用指定的凭据，停用后状态为 Disabled，无法通过接口获取该凭据的明文。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSecret(
            self,
            request: models.EnableSecretRequest,
            opts: Dict = None,
    ) -> models.EnableSecretResponse:
        """
        该接口用于开启凭据，状态为Enabled。可以通过 GetSecretValue 接口获取凭据明文。处于PendingDelete状态的凭据不能直接开启，需要通过RestoreSecret 恢复后再开启使用。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRegions(
            self,
            request: models.GetRegionsRequest,
            opts: Dict = None,
    ) -> models.GetRegionsResponse:
        """
        获取控制台展示region列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSSHKeyPairValue(
            self,
            request: models.GetSSHKeyPairValueRequest,
            opts: Dict = None,
    ) -> models.GetSSHKeyPairValueResponse:
        """
        获取SSH密钥对凭据明文信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetSSHKeyPairValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSSHKeyPairValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSecretValue(
            self,
            request: models.GetSecretValueRequest,
            opts: Dict = None,
    ) -> models.GetSecretValueResponse:
        """
        对于用户自定义凭据，通过指定凭据名称和版本来获取凭据的明文信息；
        对于云产品凭据如Mysql凭据，通过指定凭据名称和历史版本号来获取历史轮转凭据的明文信息，如果要获取当前正在使用的凭据版本的明文，需要将版本号指定为：SSM_Current。
        """
        
        kwargs = {}
        kwargs["action"] = "GetSecretValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSecretValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetServiceStatus(
            self,
            request: models.GetServiceStatusRequest,
            opts: Dict = None,
    ) -> models.GetServiceStatusResponse:
        """
        该接口用户获取用户SecretsManager服务开通状态。
        """
        
        kwargs = {}
        kwargs["action"] = "GetServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSecretVersionIds(
            self,
            request: models.ListSecretVersionIdsRequest,
            opts: Dict = None,
    ) -> models.ListSecretVersionIdsResponse:
        """
        该接口用于获取指定凭据下的版本列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListSecretVersionIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSecretVersionIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSecrets(
            self,
            request: models.ListSecretsRequest,
            opts: Dict = None,
    ) -> models.ListSecretsResponse:
        """
        该接口用于获取所有凭据的详细列表，可以指定过滤字段、排序方式等。
        """
        
        kwargs = {}
        kwargs["action"] = "ListSecrets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSecretsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PutSecretValue(
            self,
            request: models.PutSecretValueRequest,
            opts: Dict = None,
    ) -> models.PutSecretValueResponse:
        """
        该接口在指定名称的凭据下增加新版本的凭据内容，一个凭据下最多可以支持10个版本。只能对处于Enabled 和 Disabled 状态的凭据添加新的版本。
        本接口仅适用于用户自定义凭据，对云产品凭据不能操作。
        """
        
        kwargs = {}
        kwargs["action"] = "PutSecretValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PutSecretValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestoreSecret(
            self,
            request: models.RestoreSecretRequest,
            opts: Dict = None,
    ) -> models.RestoreSecretResponse:
        """
        该接口用于恢复计划删除（PendingDelete状态）中的凭据，取消计划删除。取消计划删除的凭据将处于Disabled 状态，如需恢复使用，通过EnableSecret 接口开启凭据。
        """
        
        kwargs = {}
        kwargs["action"] = "RestoreSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestoreSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RotateProductSecret(
            self,
            request: models.RotateProductSecretRequest,
            opts: Dict = None,
    ) -> models.RotateProductSecretResponse:
        """
        轮转云产品凭据或云API密钥对凭据。
        该接口仅适用于处于Enabled状态的云产品凭据或处于Enable状态的云API密钥对凭据，对于其他状态的云产品凭据或云API密钥对凭据或用户自定义凭据不适用。
        """
        
        kwargs = {}
        kwargs["action"] = "RotateProductSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RotateProductSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDescription(
            self,
            request: models.UpdateDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateDescriptionResponse:
        """
        该接口用于修改指定凭据的描述信息，仅能修改Enabled 和 Disabled 状态的凭据。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRotationStatus(
            self,
            request: models.UpdateRotationStatusRequest,
            opts: Dict = None,
    ) -> models.UpdateRotationStatusResponse:
        """
        设置云产品凭据轮转策略，可以设置：
        是否开启轮转
        轮转周期
        轮转开始时间
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRotationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRotationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSecret(
            self,
            request: models.UpdateSecretRequest,
            opts: Dict = None,
    ) -> models.UpdateSecretResponse:
        """
        该接口用于更新指定凭据名称和版本号的内容，调用该接口会对新的凭据内容加密后覆盖旧的内容。仅允许更新Enabled 和 Disabled 状态的凭据。
        本接口仅适用于用户自定义凭据，不能对云产品凭据操作。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSecret"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSecretResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)