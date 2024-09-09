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
from tencentcloud.rce.v20201103 import models


class RceClient(AbstractClient):
    _apiVersion = '2020-11-03'
    _endpoint = 'rce.tencentcloudapi.com'
    _service = 'rce'


    def CreateNameList(self, request):
        """创建黑白名单，黑白名单数量上限为100

        :param request: Request instance for CreateNameList.
        :type request: :class:`tencentcloud.rce.v20201103.models.CreateNameListRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.CreateNameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNameList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNameList(self, request):
        """修改黑白名单状态 关闭 开启 删除

        :param request: Request instance for DeleteNameList.
        :type request: :class:`tencentcloud.rce.v20201103.models.DeleteNameListRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.DeleteNameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNameList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNameListData(self, request):
        """删除黑白名单数据

        :param request: Request instance for DeleteNameListData.
        :type request: :class:`tencentcloud.rce.v20201103.models.DeleteNameListDataRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.DeleteNameListDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNameListData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNameListDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNameList(self, request):
        """列表展示黑白名单列表数据, 包含列表名称, 名单类型, 数据类型, 数据来源, 描述, 状态等

        :param request: Request instance for DescribeNameList.
        :type request: :class:`tencentcloud.rce.v20201103.models.DescribeNameListRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.DescribeNameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNameList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNameListDataList(self, request):
        """黑白名单详情数据展示 名单id 客户appid uin 数据内容 开始时间和结束时间 状态 描述

        :param request: Request instance for DescribeNameListDataList.
        :type request: :class:`tencentcloud.rce.v20201103.models.DescribeNameListDataListRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.DescribeNameListDataListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNameListDataList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNameListDataListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNameListDetail(self, request):
        """查询黑白名单列表详情

        :param request: Request instance for DescribeNameListDetail.
        :type request: :class:`tencentcloud.rce.v20201103.models.DescribeNameListDetailRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.DescribeNameListDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNameListDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNameListDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportNameListData(self, request):
        """新增黑白名单数据，所有黑白名单数据总量上限为10000

        :param request: Request instance for ImportNameListData.
        :type request: :class:`tencentcloud.rce.v20201103.models.ImportNameListDataRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.ImportNameListDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportNameListData", params, headers=headers)
            response = json.loads(body)
            model = models.ImportNameListDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ManageMarketingRisk(self, request):
        """全栈式风控引擎（RiskControlEngine，RCE）是基于人工智能技术和腾讯20年风控实战沉淀，依托腾讯海量业务构建的风控引擎，以轻量级的 SaaS 服务方式接入，帮助您快速解决注册、登录、营销活动等关键场景遇到的欺诈问题，实时防御黑灰产作恶。

        :param request: Request instance for ManageMarketingRisk.
        :type request: :class:`tencentcloud.rce.v20201103.models.ManageMarketingRiskRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.ManageMarketingRiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ManageMarketingRisk", params, headers=headers)
            response = json.loads(body)
            model = models.ManageMarketingRiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNameList(self, request):
        """修改列表数据 列表名称 列表类型 数据类型 状态 备注

        :param request: Request instance for ModifyNameList.
        :type request: :class:`tencentcloud.rce.v20201103.models.ModifyNameListRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.ModifyNameListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNameList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNameListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNameListData(self, request):
        """修改黑白名单列表详情 详情内容 开始和结束时间 状态 备注等

        :param request: Request instance for ModifyNameListData.
        :type request: :class:`tencentcloud.rce.v20201103.models.ModifyNameListDataRequest`
        :rtype: :class:`tencentcloud.rce.v20201103.models.ModifyNameListDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNameListData", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNameListDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))