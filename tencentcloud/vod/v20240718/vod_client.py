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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.vod.v20240718 import models


class VodClient(AbstractClient):
    _apiVersion = '2024-07-18'
    _endpoint = 'vod.tencentcloudapi.com'
    _service = 'vod'


    def CreateIncrementalMigrationStrategy(self, request):
        r"""创建增量迁移策略。

        :param request: Request instance for CreateIncrementalMigrationStrategy.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateIncrementalMigrationStrategyRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateIncrementalMigrationStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIncrementalMigrationStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIncrementalMigrationStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStorage(self, request):
        r"""该接口用于为专业版应用创建存储桶。

        注：
        - 本接口仅用于专业版应用；
        - 客户创建点播专业版应用时，系统默认为客户开通了部分地域的存储，用户如果需要开通其它地域的存储，可以通过该接口进行开通；
        - 通过 [DescribeStorageRegions](https://cloud.tencent.com/document/product/266/72480) 接口可以查询到所有存储地域及已经开通存储桶的地域。

        :param request: Request instance for CreateStorage.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateStorageRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStorageCredentials(self, request):
        r"""用于按指定策略，生成专业版应用的临时访问凭证，比如生成用于客户端上传的临时凭证。

        :param request: Request instance for CreateStorageCredentials.
        :type request: :class:`tencentcloud.vod.v20240718.models.CreateStorageCredentialsRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.CreateStorageCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStorageCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStorageCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIncrementalMigrationStrategy(self, request):
        r"""删除增量迁移策略。

        :param request: Request instance for DeleteIncrementalMigrationStrategy.
        :type request: :class:`tencentcloud.vod.v20240718.models.DeleteIncrementalMigrationStrategyRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.DeleteIncrementalMigrationStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIncrementalMigrationStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIncrementalMigrationStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIncrementalMigrationStrategyInfos(self, request):
        r"""查询增量迁移策略信息。

        :param request: Request instance for DescribeIncrementalMigrationStrategyInfos.
        :type request: :class:`tencentcloud.vod.v20240718.models.DescribeIncrementalMigrationStrategyInfosRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.DescribeIncrementalMigrationStrategyInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIncrementalMigrationStrategyInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIncrementalMigrationStrategyInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStorage(self, request):
        r"""该接口用于查询专业版应用中的存储桶信息，同时支持分页查询。

        注：
        - 本接口仅用于专业版应用。

        :param request: Request instance for DescribeStorage.
        :type request: :class:`tencentcloud.vod.v20240718.models.DescribeStorageRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.DescribeStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStorage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStorageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIncrementalMigrationStrategy(self, request):
        r"""创建增量迁移策略。

        :param request: Request instance for ModifyIncrementalMigrationStrategy.
        :type request: :class:`tencentcloud.vod.v20240718.models.ModifyIncrementalMigrationStrategyRequest`
        :rtype: :class:`tencentcloud.vod.v20240718.models.ModifyIncrementalMigrationStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIncrementalMigrationStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIncrementalMigrationStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))