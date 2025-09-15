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
from tencentcloud.igtm.v20231024 import models


class IgtmClient(AbstractClient):
    _apiVersion = '2023-10-24'
    _endpoint = 'igtm.tencentcloudapi.com'
    _service = 'igtm'


    def CreateAddressPool(self, request):
        r"""创建地址池

        :param request: Request instance for CreateAddressPool.
        :type request: :class:`tencentcloud.igtm.v20231024.models.CreateAddressPoolRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.CreateAddressPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressPool", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        r"""创建实例接口，仅供免费实例使用

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.igtm.v20231024.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMonitor(self, request):
        r"""新增监控器

        :param request: Request instance for CreateMonitor.
        :type request: :class:`tencentcloud.igtm.v20231024.models.CreateMonitorRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.CreateMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStrategy(self, request):
        r"""新建策略接口

        :param request: Request instance for CreateStrategy.
        :type request: :class:`tencentcloud.igtm.v20231024.models.CreateStrategyRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.CreateStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressPool(self, request):
        r"""删除地址池

        :param request: Request instance for DeleteAddressPool.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DeleteAddressPoolRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DeleteAddressPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressPool", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMonitor(self, request):
        r"""删除监控器

        :param request: Request instance for DeleteMonitor.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DeleteMonitorRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DeleteMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStrategy(self, request):
        r"""删除策略接口

        :param request: Request instance for DeleteStrategy.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DeleteStrategyRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DeleteStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressLocation(self, request):
        r"""获取地址所属地域

        :param request: Request instance for DescribeAddressLocation.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeAddressLocationRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeAddressLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressPoolDetail(self, request):
        r"""地址池详情

        :param request: Request instance for DescribeAddressPoolDetail.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeAddressPoolDetailRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeAddressPoolDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressPoolDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressPoolDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressPoolList(self, request):
        r"""地址池列表

        :param request: Request instance for DescribeAddressPoolList.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeAddressPoolListRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeAddressPoolListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressPoolList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressPoolListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDetectPackageDetail(self, request):
        r"""探测任务包详情

        :param request: Request instance for DescribeDetectPackageDetail.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeDetectPackageDetailRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeDetectPackageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDetectPackageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDetectPackageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDetectTaskPackageList(self, request):
        r"""探测任务套餐列表

        :param request: Request instance for DescribeDetectTaskPackageList.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeDetectTaskPackageListRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeDetectTaskPackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDetectTaskPackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDetectTaskPackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDetectors(self, request):
        r"""获取探测节点列表接口

        :param request: Request instance for DescribeDetectors.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeDetectorsRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeDetectorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDetectors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDetectorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDnsLineList(self, request):
        r"""查询分组线路列表接口

        :param request: Request instance for DescribeDnsLineList.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeDnsLineListRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeDnsLineListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDnsLineList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDnsLineListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDetail(self, request):
        r"""实例详情

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceList(self, request):
        r"""实例列表

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancePackageList(self, request):
        r"""实例套餐列表

        :param request: Request instance for DescribeInstancePackageList.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeInstancePackageListRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeInstancePackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancePackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancePackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonitorDetail(self, request):
        r"""查询监控器详情接口

        :param request: Request instance for DescribeMonitorDetail.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeMonitorDetailRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMonitors(self, request):
        r"""获取所有监控器

        :param request: Request instance for DescribeMonitors.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeMonitorsRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeMonitorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeQuotas(self, request):
        r"""配额查询

        :param request: Request instance for DescribeQuotas.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeQuotasRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyDetail(self, request):
        r"""策略详情

        :param request: Request instance for DescribeStrategyDetail.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeStrategyDetailRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeStrategyDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStrategyList(self, request):
        r"""策略列表接口

        :param request: Request instance for DescribeStrategyList.
        :type request: :class:`tencentcloud.igtm.v20231024.models.DescribeStrategyListRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.DescribeStrategyListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStrategyList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStrategyListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressPool(self, request):
        r"""修改地址池

        :param request: Request instance for ModifyAddressPool.
        :type request: :class:`tencentcloud.igtm.v20231024.models.ModifyAddressPoolRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.ModifyAddressPoolResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressPool", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressPoolResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceConfig(self, request):
        r"""修改实例配置

        :param request: Request instance for ModifyInstanceConfig.
        :type request: :class:`tencentcloud.igtm.v20231024.models.ModifyInstanceConfigRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.ModifyInstanceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMonitor(self, request):
        r"""修改监控器

        :param request: Request instance for ModifyMonitor.
        :type request: :class:`tencentcloud.igtm.v20231024.models.ModifyMonitorRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.ModifyMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStrategy(self, request):
        r"""修改策略接口

        :param request: Request instance for ModifyStrategy.
        :type request: :class:`tencentcloud.igtm.v20231024.models.ModifyStrategyRequest`
        :rtype: :class:`tencentcloud.igtm.v20231024.models.ModifyStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))