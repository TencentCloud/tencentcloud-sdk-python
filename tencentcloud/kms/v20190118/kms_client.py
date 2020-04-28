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
from tencentcloud.kms.v20190118 import models


class KmsClient(AbstractClient):
    _apiVersion = '2019-01-18'
    _endpoint = 'kms.tencentcloudapi.com'


    def AsymmetricRsaDecrypt(self, request):
        """使用指定的RSA非对称密钥的私钥进行数据解密，密文必须是使用对应公钥加密的。处于Enabled 状态的非对称密钥才能进行解密操作。

        :param request: Request instance for AsymmetricRsaDecrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.AsymmetricRsaDecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.AsymmetricRsaDecryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AsymmetricRsaDecrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AsymmetricRsaDecryptResponse()
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


    def AsymmetricSm2Decrypt(self, request):
        """使用指定的SM2非对称密钥的私钥进行数据解密，密文必须是使用对应公钥加密的。处于Enabled 状态的非对称密钥才能进行解密操作。传入的密文的长度不能超过256字节。

        :param request: Request instance for AsymmetricSm2Decrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.AsymmetricSm2DecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.AsymmetricSm2DecryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AsymmetricSm2Decrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AsymmetricSm2DecryptResponse()
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


    def CancelKeyDeletion(self, request):
        """取消CMK的计划删除操作

        :param request: Request instance for CancelKeyDeletion.
        :type request: :class:`tencentcloud.kms.v20190118.models.CancelKeyDeletionRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CancelKeyDeletionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelKeyDeletion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelKeyDeletionResponse()
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


    def CreateKey(self, request):
        """创建用户管理数据密钥的主密钥CMK（Custom Master Key）。

        :param request: Request instance for CreateKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.CreateKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CreateKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateKeyResponse()
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


    def CreateWhiteBoxKey(self, request):
        """创建白盒密钥。 密钥个数的上限为 50。

        :param request: Request instance for CreateWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.CreateWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.CreateWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWhiteBoxKeyResponse()
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


    def Decrypt(self, request):
        """本接口用于解密密文，得到明文数据。

        :param request: Request instance for Decrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.DecryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DecryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Decrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DecryptResponse()
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


    def DeleteImportedKeyMaterial(self, request):
        """用于删除导入的密钥材料，仅对EXTERNAL类型的CMK有效，该接口将CMK设置为PendingImport 状态，并不会删除CMK，在重新进行密钥导入后可继续使用。彻底删除CMK请使用 ScheduleKeyDeletion 接口。

        :param request: Request instance for DeleteImportedKeyMaterial.
        :type request: :class:`tencentcloud.kms.v20190118.models.DeleteImportedKeyMaterialRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DeleteImportedKeyMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImportedKeyMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImportedKeyMaterialResponse()
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


    def DeleteWhiteBoxKey(self, request):
        """删除白盒密钥, 注意：必须先禁用后，才可以删除。

        :param request: Request instance for DeleteWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DeleteWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DeleteWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWhiteBoxKeyResponse()
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


    def DescribeKey(self, request):
        """用于获取指定KeyId的主密钥属性详情信息。

        :param request: Request instance for DescribeKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeyResponse()
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


    def DescribeKeys(self, request):
        """该接口用于批量获取主密钥属性信息。

        :param request: Request instance for DescribeKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeysResponse()
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


    def DescribeWhiteBoxDecryptKey(self, request):
        """获取白盒解密密钥

        :param request: Request instance for DescribeWhiteBoxDecryptKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxDecryptKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxDecryptKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxDecryptKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxDecryptKeyResponse()
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


    def DescribeWhiteBoxKey(self, request):
        """展示白盒密钥的信息

        :param request: Request instance for DescribeWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxKeyResponse()
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


    def DescribeWhiteBoxKeyDetails(self, request):
        """获取白盒密钥列表

        :param request: Request instance for DescribeWhiteBoxKeyDetails.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyDetailsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxKeyDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxKeyDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxKeyDetailsResponse()
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


    def DescribeWhiteBoxServiceStatus(self, request):
        """获取白盒密钥服务状态

        :param request: Request instance for DescribeWhiteBoxServiceStatus.
        :type request: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxServiceStatusRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DescribeWhiteBoxServiceStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWhiteBoxServiceStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWhiteBoxServiceStatusResponse()
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


    def DisableKey(self, request):
        """本接口用于禁用一个主密钥，处于禁用状态的Key无法用于加密、解密操作。

        :param request: Request instance for DisableKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableKeyResponse()
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


    def DisableKeyRotation(self, request):
        """对指定的CMK禁止密钥轮换功能。

        :param request: Request instance for DisableKeyRotation.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableKeyRotationRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableKeyRotationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableKeyRotation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableKeyRotationResponse()
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


    def DisableKeys(self, request):
        """该接口用于批量禁止CMK的使用。

        :param request: Request instance for DisableKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableKeysResponse()
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


    def DisableWhiteBoxKey(self, request):
        """禁用白盒密钥

        :param request: Request instance for DisableWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableWhiteBoxKeyResponse()
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


    def DisableWhiteBoxKeys(self, request):
        """批量禁用白盒密钥

        :param request: Request instance for DisableWhiteBoxKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.DisableWhiteBoxKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableWhiteBoxKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableWhiteBoxKeysResponse()
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


    def EnableKey(self, request):
        """用于启用一个指定的CMK。

        :param request: Request instance for EnableKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableKeyResponse()
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


    def EnableKeyRotation(self, request):
        """对指定的CMK开启密钥轮换功能。

        :param request: Request instance for EnableKeyRotation.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableKeyRotationRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableKeyRotationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableKeyRotation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableKeyRotationResponse()
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


    def EnableKeys(self, request):
        """该接口用于批量启用CMK。

        :param request: Request instance for EnableKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableKeysResponse()
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


    def EnableWhiteBoxKey(self, request):
        """启用白盒密钥

        :param request: Request instance for EnableWhiteBoxKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableWhiteBoxKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableWhiteBoxKeyResponse()
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


    def EnableWhiteBoxKeys(self, request):
        """批量启用白盒密钥

        :param request: Request instance for EnableWhiteBoxKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EnableWhiteBoxKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableWhiteBoxKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableWhiteBoxKeysResponse()
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


    def Encrypt(self, request):
        """本接口用于加密最多为4KB任意数据，可用于加密数据库密码，RSA Key，或其它较小的敏感信息。对于应用的数据加密，使用GenerateDataKey生成的DataKey进行本地数据的加解密操作

        :param request: Request instance for Encrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.EncryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EncryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Encrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EncryptResponse()
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


    def EncryptByWhiteBox(self, request):
        """使用白盒密钥进行加密

        :param request: Request instance for EncryptByWhiteBox.
        :type request: :class:`tencentcloud.kms.v20190118.models.EncryptByWhiteBoxRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.EncryptByWhiteBoxResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EncryptByWhiteBox", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EncryptByWhiteBoxResponse()
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


    def GenerateDataKey(self, request):
        """本接口生成一个数据密钥，您可以用这个密钥进行本地数据的加密。

        :param request: Request instance for GenerateDataKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.GenerateDataKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GenerateDataKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateDataKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateDataKeyResponse()
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


    def GenerateRandom(self, request):
        """随机数生成接口。

        :param request: Request instance for GenerateRandom.
        :type request: :class:`tencentcloud.kms.v20190118.models.GenerateRandomRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GenerateRandomResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GenerateRandom", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateRandomResponse()
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


    def GetKeyRotationStatus(self, request):
        """查询指定的CMK是否开启了密钥轮换功能。

        :param request: Request instance for GetKeyRotationStatus.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetKeyRotationStatusRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetKeyRotationStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetKeyRotationStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetKeyRotationStatusResponse()
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


    def GetParametersForImport(self, request):
        """获取导入主密钥（CMK）材料的参数，返回的Token作为执行ImportKeyMaterial的参数之一，返回的PublicKey用于对自主导入密钥材料进行加密。返回的Token和PublicKey 24小时后失效，失效后如需重新导入，需要再次调用该接口获取新的Token和PublicKey。

        :param request: Request instance for GetParametersForImport.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetParametersForImportRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetParametersForImportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetParametersForImport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetParametersForImportResponse()
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


    def GetPublicKey(self, request):
        """该接口用户获取 KeyUsage为ASYMMETRIC_DECRYPT_RSA_2048 和 ASYMMETRIC_DECRYPT_SM2 的非对称密钥的公钥信息，使用该公钥用户可在本地进行数据加密，使用该公钥加密的数据只能通过KMS使用对应的私钥进行解密。只有处于Enabled状态的非对称密钥才可能获取公钥。

        :param request: Request instance for GetPublicKey.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetPublicKeyRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetPublicKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetPublicKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPublicKeyResponse()
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
        """用于查询该用户是否已开通KMS服务

        :param request: Request instance for GetServiceStatus.
        :type request: :class:`tencentcloud.kms.v20190118.models.GetServiceStatusRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.GetServiceStatusResponse`

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


    def ImportKeyMaterial(self, request):
        """用于导入密钥材料。只有类型为EXTERNAL 的CMK 才可以导入，导入的密钥材料使用 GetParametersForImport 获取的密钥进行加密。可以为指定的 CMK 重新导入密钥材料，并重新指定过期时间，但必须导入相同的密钥材料。CMK 密钥材料导入后不可以更换密钥材料。导入的密钥材料过期或者被删除后，指定的CMK将无法使用，需要再次导入相同的密钥材料才能正常使用。CMK是独立的，同样的密钥材料可导入不同的 CMK 中，但使用其中一个 CMK 加密的数据无法使用另一个 CMK解密。
        只有Enabled 和 PendingImport状态的CMK可以导入密钥材料。

        :param request: Request instance for ImportKeyMaterial.
        :type request: :class:`tencentcloud.kms.v20190118.models.ImportKeyMaterialRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ImportKeyMaterialResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportKeyMaterial", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportKeyMaterialResponse()
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


    def ListAlgorithms(self, request):
        """列出当前Region支持的加密方式

        :param request: Request instance for ListAlgorithms.
        :type request: :class:`tencentcloud.kms.v20190118.models.ListAlgorithmsRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ListAlgorithmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAlgorithms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAlgorithmsResponse()
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


    def ListKeyDetail(self, request):
        """根据指定Offset和Limit获取主密钥列表详情。

        :param request: Request instance for ListKeyDetail.
        :type request: :class:`tencentcloud.kms.v20190118.models.ListKeyDetailRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ListKeyDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListKeyDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListKeyDetailResponse()
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


    def ListKeys(self, request):
        """列出账号下面状态为Enabled， Disabled 和 PendingImport 的CMK KeyId 列表

        :param request: Request instance for ListKeys.
        :type request: :class:`tencentcloud.kms.v20190118.models.ListKeysRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ListKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListKeysResponse()
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


    def ReEncrypt(self, request):
        """使用指定CMK对密文重新加密。

        :param request: Request instance for ReEncrypt.
        :type request: :class:`tencentcloud.kms.v20190118.models.ReEncryptRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ReEncryptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReEncrypt", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReEncryptResponse()
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


    def ScheduleKeyDeletion(self, request):
        """CMK计划删除接口，用于指定CMK删除的时间，可选时间区间为[7,30]天

        :param request: Request instance for ScheduleKeyDeletion.
        :type request: :class:`tencentcloud.kms.v20190118.models.ScheduleKeyDeletionRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.ScheduleKeyDeletionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ScheduleKeyDeletion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScheduleKeyDeletionResponse()
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


    def UpdateAlias(self, request):
        """用于修改CMK的别名。对于处于PendingDelete状态的CMK禁止修改。

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.kms.v20190118.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAliasResponse()
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


    def UpdateKeyDescription(self, request):
        """该接口用于对指定的cmk修改描述信息。对于处于PendingDelete状态的CMK禁止修改。

        :param request: Request instance for UpdateKeyDescription.
        :type request: :class:`tencentcloud.kms.v20190118.models.UpdateKeyDescriptionRequest`
        :rtype: :class:`tencentcloud.kms.v20190118.models.UpdateKeyDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateKeyDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateKeyDescriptionResponse()
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