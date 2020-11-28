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
from tencentcloud.ssm.v20190923 import models


class SsmClient(AbstractClient):
    _apiVersion = '2019-09-23'
    _endpoint = 'ssm.tencentcloudapi.com'
    _service = 'ssm'


    def CreateSecret(self, request):
        """创建新的凭据信息，通过KMS进行加密保护。每个Region最多可创建存储1000个凭据信息。

        :param request: Request instance for CreateSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.CreateSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.CreateSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecretResponse()
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


    def DeleteSecret(self, request):
        """删除指定的凭据信息，可以通过RecoveryWindowInDays参数设置立即删除或者计划删除。对于计划删除的凭据，在删除日期到达之前状态为 PendingDelete，并可以通过RestoreSecret 进行恢复，超出指定删除日期之后会被彻底删除。您必须先通过 DisableSecret 停用凭据后才可以进行（计划）删除操作。

        :param request: Request instance for DeleteSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecretResponse()
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


    def DeleteSecretVersion(self, request):
        """该接口用于直接删除指定凭据下的单个版本凭据，删除操作立即生效，对所有状态下的凭据版本都可以删除。

        :param request: Request instance for DeleteSecretVersion.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretVersionRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DeleteSecretVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecretVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecretVersionResponse()
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


    def DescribeSecret(self, request):
        """获取凭据的详细属性信息。

        :param request: Request instance for DescribeSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DescribeSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DescribeSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecretResponse()
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


    def DisableSecret(self, request):
        """停用指定的凭据，停用后状态为 Disabled，无法通过接口获取该凭据的明文。

        :param request: Request instance for DisableSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.DisableSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.DisableSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableSecretResponse()
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


    def EnableSecret(self, request):
        """该接口用于开启凭据，状态为Enabled。可以通过 GetSecretValue 接口获取凭据明文。处于PendingDelete状态的凭据不能直接开启，需要通过RestoreSecret 恢复后再开启使用。

        :param request: Request instance for EnableSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.EnableSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.EnableSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableSecretResponse()
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


    def GetRegions(self, request):
        """获取控制台展示region列表

        :param request: Request instance for GetRegions.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetRegionsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRegionsResponse()
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


    def GetSecretValue(self, request):
        """获取指定凭据名称和版本的凭据明文信息，只能获取启用状态的凭据明文。

        :param request: Request instance for GetSecretValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetSecretValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetSecretValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetSecretValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetSecretValueResponse()
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


    def GetServiceStatus(self, request):
        """该接口用户获取用户SecretsManager服务开通状态。

        :param request: Request instance for GetServiceStatus.
        :type request: :class:`tencentcloud.ssm.v20190923.models.GetServiceStatusRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.GetServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetServiceStatusResponse()
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


    def ListSecretVersionIds(self, request):
        """该接口用于获取指定凭据下的版本列表信息

        :param request: Request instance for ListSecretVersionIds.
        :type request: :class:`tencentcloud.ssm.v20190923.models.ListSecretVersionIdsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.ListSecretVersionIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSecretVersionIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSecretVersionIdsResponse()
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


    def ListSecrets(self, request):
        """该接口用于获取所有凭据的详细列表，可以指定过滤字段、排序方式等。

        :param request: Request instance for ListSecrets.
        :type request: :class:`tencentcloud.ssm.v20190923.models.ListSecretsRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.ListSecretsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListSecrets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListSecretsResponse()
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


    def PutSecretValue(self, request):
        """该接口在指定名称的凭据下增加新版本的凭据内容，一个凭据下最多可以支持10个版本。只能对处于Enabled 和 Disabled 状态的凭据添加新的版本。

        :param request: Request instance for PutSecretValue.
        :type request: :class:`tencentcloud.ssm.v20190923.models.PutSecretValueRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.PutSecretValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutSecretValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutSecretValueResponse()
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


    def RestoreSecret(self, request):
        """该接口用于恢复计划删除（PendingDelete状态）中的凭据，取消计划删除。取消计划删除的凭据将处于Disabled 状态，如需恢复使用，通过EnableSecret 接口开启凭据。

        :param request: Request instance for RestoreSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.RestoreSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.RestoreSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreSecretResponse()
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


    def UpdateDescription(self, request):
        """该接口用于修改指定凭据的描述信息，仅能修改Enabled 和 Disabled 状态的凭据。

        :param request: Request instance for UpdateDescription.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateDescriptionRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDescriptionResponse()
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


    def UpdateSecret(self, request):
        """该接口用于更新指定凭据名称和版本号的内容，调用该接口会对新的凭据内容加密后覆盖旧的内容。仅允许更新Enabled 和 Disabled 状态的凭据。

        :param request: Request instance for UpdateSecret.
        :type request: :class:`tencentcloud.ssm.v20190923.models.UpdateSecretRequest`
        :rtype: :class:`tencentcloud.ssm.v20190923.models.UpdateSecretResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateSecret", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateSecretResponse()
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