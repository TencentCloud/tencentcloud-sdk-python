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
from tencentcloud.drm.v20181115 import models


class DrmClient(AbstractClient):
    _apiVersion = '2018-11-15'
    _endpoint = 'drm.tencentcloudapi.com'


    def CreateLicense(self, request):
        """本接口用来生成DRM方案对应的播放许可证，开发者需提供DRM方案类型、内容类型参数，后台将生成许可证后返回许可证数据
        开发者需要转发终端设备发出的许可证请求信息。

        :param request: 调用CreateLicense所需参数的结构体。
        :type request: :class:`tencentcloud.drm.v20181115.models.CreateLicenseRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.CreateLicenseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLicense", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLicenseResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKeys(self, request):
        """开发者需要指定使用的DRM类型、和需要加密的Track类型，后台返回加密使用的密钥
        如果加密使用的ContentID没有关联的密钥信息，后台会自动生成新的密钥返回

        :param request: 调用DescribeKeys所需参数的结构体。
        :type request: :class:`tencentcloud.drm.v20181115.models.DescribeKeysRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.DescribeKeysResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartEncryption(self, request):
        """开发者调用该接口，启动一次内容文件的DRM加密工作流

        :param request: 调用StartEncryption所需参数的结构体。
        :type request: :class:`tencentcloud.drm.v20181115.models.StartEncryptionRequest`
        :rtype: :class:`tencentcloud.drm.v20181115.models.StartEncryptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartEncryption", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartEncryptionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)