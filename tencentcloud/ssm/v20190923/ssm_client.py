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
from tencentcloud.ssm.v20190923 import models


class SsmClient(AbstractClient):
    _apiVersion = '2019-09-23'
    _endpoint = 'ssm.tencentcloudapi.com'
    _service = 'ssm'


    def CreateProductSecret(self, request):
        """创建云产品凭据

        :param request: Request instance for CreateProductSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateProductSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateProductSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProductSecret", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProductSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSSHKeyPairSecret(self, request):
        """创建用于托管SSH密钥对的凭据

        :param request: Request instance for CreateSSHKeyPairSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateSSHKeyPairSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateSSHKeyPairSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSSHKeyPairSecret", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSSHKeyPairSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecret(self, request):
        """创建新的凭据信息，通过KMS进行加密保护。每个Region最多可创建存储1000个凭据信息。

        :param request: Request instance for CreateSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecret", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecret(self, request):
        """删除指定的凭据信息，可以通过RecoveryWindowInDays参数设置立即删除或者计划删除。对于计划删除的凭据，在删除日期到达之前状态为 PendingDelete，并可以通过RestoreSecret 进行恢复，超出指定删除日期之后会被彻底删除。您必须先通过 DisableSecret 停用凭据后才可以进行（计划）删除操作。

        :param request: Request instance for DeleteSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecretVersion(self, request):
        """该接口用于直接删除指定凭据下的单个版本凭据，删除操作立即生效，对所有状态下的凭据版本都可以删除。
        本接口仅适用于用户自定义凭据，本接口不能对云产品凭据进行操作。

        :param request: Request instance for DeleteSecretVersion.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretVersionRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecretVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecretVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAsyncRequestInfo(self, request):
        """查询异步任务的执行结果

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncRequestInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncRequestInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRotationDetail(self, request):
        """查询凭据轮转策略详情。
        本接口只适用于云产品凭据。

        :param request: Request instance for DescribeRotationDetail.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationDetailRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRotationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRotationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRotationHistory(self, request):
        """查询凭据轮转历史版本。
        本接口仅适用于云产品凭据。

        :param request: Request instance for DescribeRotationHistory.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationHistoryRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeRotationHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRotationHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRotationHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecret(self, request):
        """获取凭据的详细属性信息。

        :param request: Request instance for DescribeSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSupportedProducts(self, request):
        """查询支持的云产品列表

        :param request: Request instance for DescribeSupportedProducts.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeSupportedProductsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeSupportedProductsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportedProducts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportedProductsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableSecret(self, request):
        """停用指定的凭据，停用后状态为 Disabled，无法通过接口获取该凭据的明文。

        :param request: Request instance for DisableSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DisableSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DisableSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableSecret", params, headers=headers)
            response = json.loads(body)
            model = models.DisableSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableSecret(self, request):
        """该接口用于开启凭据，状态为Enabled。可以通过 GetSecretValue 接口获取凭据明文。处于PendingDelete状态的凭据不能直接开启，需要通过RestoreSecret 恢复后再开启使用。

        :param request: Request instance for EnableSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.EnableSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.EnableSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableSecret", params, headers=headers)
            response = json.loads(body)
            model = models.EnableSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRegions(self, request):
        """获取控制台展示region列表

        :param request: Request instance for GetRegions.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetRegionsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRegions", params, headers=headers)
            response = json.loads(body)
            model = models.GetRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSSHKeyPairValue(self, request):
        """获取SSH密钥对凭据明文信息。

        :param request: Request instance for GetSSHKeyPairValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetSSHKeyPairValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetSSHKeyPairValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSSHKeyPairValue", params, headers=headers)
            response = json.loads(body)
            model = models.GetSSHKeyPairValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetSecretValue(self, request):
        """对于用户自定义凭据，通过指定凭据名称和版本来获取凭据的明文信息；
        对于云产品凭据如Mysql凭据，通过指定凭据名称和历史版本号来获取历史轮转凭据的明文信息，如果要获取当前正在使用的凭据版本的明文，需要将版本号指定为：SSM_Current。

        :param request: Request instance for GetSecretValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetSecretValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetSecretValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetSecretValue", params, headers=headers)
            response = json.loads(body)
            model = models.GetSecretValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetServiceStatus(self, request):
        """该接口用户获取用户SecretsManager服务开通状态。

        :param request: Request instance for GetServiceStatus.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetServiceStatusRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetServiceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.GetServiceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListSecretVersionIds(self, request):
        """该接口用于获取指定凭据下的版本列表信息

        :param request: Request instance for ListSecretVersionIds.
        :type request: :class:`tencentcloud.ssm.v20190923.models.ListSecretVersionIdsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.ListSecretVersionIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSecretVersionIds", params, headers=headers)
            response = json.loads(body)
            model = models.ListSecretVersionIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListSecrets(self, request):
        """该接口用于获取所有凭据的详细列表，可以指定过滤字段、排序方式等。

        :param request: Request instance for ListSecrets.
        :type request: :class:`tencentcloud.ssm.v20190923.models.ListSecretsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.ListSecretsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListSecrets", params, headers=headers)
            response = json.loads(body)
            model = models.ListSecretsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PutSecretValue(self, request):
        """该接口在指定名称的凭据下增加新版本的凭据内容，一个凭据下最多可以支持10个版本。只能对处于Enabled 和 Disabled 状态的凭据添加新的版本。
        本接口仅适用于用户自定义凭据，对云产品凭据不能操作。

        :param request: Request instance for PutSecretValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.PutSecretValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.PutSecretValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutSecretValue", params, headers=headers)
            response = json.loads(body)
            model = models.PutSecretValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestoreSecret(self, request):
        """该接口用于恢复计划删除（PendingDelete状态）中的凭据，取消计划删除。取消计划删除的凭据将处于Disabled 状态，如需恢复使用，通过EnableSecret 接口开启凭据。

        :param request: Request instance for RestoreSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.RestoreSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.RestoreSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreSecret", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RotateProductSecret(self, request):
        """轮转云产品凭据或云API密钥对凭据。
        该接口仅适用于处于Enabled状态的云产品凭据或处于Enable状态的云API密钥对凭据，对于其他状态的云产品凭据或云API密钥对凭据或用户自定义凭据不适用。

        :param request: Request instance for RotateProductSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.RotateProductSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.RotateProductSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RotateProductSecret", params, headers=headers)
            response = json.loads(body)
            model = models.RotateProductSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDescription(self, request):
        """该接口用于修改指定凭据的描述信息，仅能修改Enabled 和 Disabled 状态的凭据。

        :param request: Request instance for UpdateDescription.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateDescriptionRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDescription", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRotationStatus(self, request):
        """设置云产品凭据轮转策略，可以设置：
        是否开启轮转
        轮转周期
        轮转开始时间

        :param request: Request instance for UpdateRotationStatus.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateRotationStatusRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateRotationStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRotationStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRotationStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateSecret(self, request):
        """该接口用于更新指定凭据名称和版本号的内容，调用该接口会对新的凭据内容加密后覆盖旧的内容。仅允许更新Enabled 和 Disabled 状态的凭据。
        本接口仅适用于用户自定义凭据，不能对云产品凭据操作。

        :param request: Request instance for UpdateSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateSecretResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateSecret", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateSecretResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)