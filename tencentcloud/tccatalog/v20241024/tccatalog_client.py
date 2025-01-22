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
from tencentcloud.tccatalog.v20241024 import models


class TccatalogClient(AbstractClient):
    _apiVersion = '2024-10-24'
    _endpoint = 'tccatalog.tencentcloudapi.com'
    _service = 'tccatalog'


    def AcceptTccVpcEndPointConnect(self, request):
        """接受终端节点连接

        :param request: Request instance for AcceptTccVpcEndPointConnect.
        :type request: :class:`tencentcloud.tccatalog.v20241024.models.AcceptTccVpcEndPointConnectRequest`
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.AcceptTccVpcEndPointConnectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptTccVpcEndPointConnect", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptTccVpcEndPointConnectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindTccVpcEndPointServiceWhiteList(self, request):
        """绑定终端节点服务白名单用户

        :param request: Request instance for BindTccVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.tccatalog.v20241024.models.BindTccVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.BindTccVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindTccVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.BindTccVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTccCatalog(self, request):
        """获取Tcc数据目录详情

        :param request: Request instance for DescribeTccCatalog.
        :type request: :class:`tencentcloud.tccatalog.v20241024.models.DescribeTccCatalogRequest`
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.DescribeTccCatalogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTccCatalog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTccCatalogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTccCatalogs(self, request):
        """获取Tcc数据目录列表

        :param request: Request instance for DescribeTccCatalogs.
        :type request: :class:`tencentcloud.tccatalog.v20241024.models.DescribeTccCatalogsRequest`
        :rtype: :class:`tencentcloud.tccatalog.v20241024.models.DescribeTccCatalogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTccCatalogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTccCatalogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))