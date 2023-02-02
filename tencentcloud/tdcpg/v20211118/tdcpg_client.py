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
from tencentcloud.tdcpg.v20211118 import models


class TdcpgClient(AbstractClient):
    _apiVersion = '2021-11-18'
    _endpoint = 'tdcpg.tencentcloudapi.com'
    _service = 'tdcpg'


    def CloneClusterToPointInTime(self, request):
        """使用指定时间点的备份克隆一个新的集群

        :param request: Request instance for CloneClusterToPointInTime.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.CloneClusterToPointInTimeRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.CloneClusterToPointInTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneClusterToPointInTime", params, headers=headers)
            response = json.loads(body)
            model = models.CloneClusterToPointInTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCluster(self, request):
        """创建集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateClusterInstances(self, request):
        """在集群中新建实例

        :param request: Request instance for CreateClusterInstances.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.CreateClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.CreateClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCluster(self, request):
        """删除集群，集群中的实例和数据都将被删除，且无法恢复。只有当集群状态处于isolated(已隔离)时才生效。

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteClusterInstances(self, request):
        """删除实例。只有当实例状态处于isolated(已隔离)时才生效。

        :param request: Request instance for DeleteClusterInstances.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DeleteClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DeleteClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccounts(self, request):
        """查询数据库账号信息

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterBackups(self, request):
        """查询集群的备份集

        :param request: Request instance for DescribeClusterBackups.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterBackupsRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterEndpoints(self, request):
        """查询集群接入点信息

        :param request: Request instance for DescribeClusterEndpoints.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterEndpointsRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterEndpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEndpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterEndpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterInstances(self, request):
        """查询实例

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterRecoveryTimeRange(self, request):
        """查询集群可回档时间范围

        :param request: Request instance for DescribeClusterRecoveryTimeRange.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterRecoveryTimeRangeRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClusterRecoveryTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterRecoveryTimeRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterRecoveryTimeRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusters(self, request):
        """查询集群

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourcesByDealName(self, request):
        """根据订单号获取资源信息

        :param request: Request instance for DescribeResourcesByDealName.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.DescribeResourcesByDealNameRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.DescribeResourcesByDealNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByDealName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesByDealNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateCluster(self, request):
        """隔离集群，集群的接入点网络将会断掉无法连接使用数据库。只有当集群状态处于running(运行中)时才生效。

        :param request: Request instance for IsolateCluster.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.IsolateClusterRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.IsolateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateClusterInstances(self, request):
        """隔离实例。此接口只针对状态为running的实例生效，使用场景包括：
         - 批量隔离集群内所有的实例
         - 在读写实例为running(运行中)时，单个/批量隔离只读实例
         - 集群内所有只读实例为isolated(已隔离)时，单独隔离读写实例

        :param request: Request instance for IsolateClusterInstances.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.IsolateClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.IsolateClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccountDescription(self, request):
        """修改数据库账号描述

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterEndpointWanStatus(self, request):
        """开启或者关闭接入点外网

        :param request: Request instance for ModifyClusterEndpointWanStatus.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClusterEndpointWanStatusRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClusterEndpointWanStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterEndpointWanStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterEndpointWanStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterInstancesSpec(self, request):
        """修改实例规格，此接口只针对状态为running(运行中)的实例生效

        :param request: Request instance for ModifyClusterInstancesSpec.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClusterInstancesSpecRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClusterInstancesSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterInstancesSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterInstancesSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterName(self, request):
        """修改集群名字

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClustersAutoRenewFlag(self, request):
        """修改集群自动续费，只对预付费集群生效。

        :param request: Request instance for ModifyClustersAutoRenewFlag.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClustersAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.ModifyClustersAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClustersAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClustersAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverCluster(self, request):
        """恢复集群，恢复集群的接入点网络，恢复后继续连接使用数据库。只有当集群状态处于isolated(已隔离)时才生效。

        :param request: Request instance for RecoverCluster.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.RecoverClusterRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.RecoverClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverCluster", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverClusterInstances(self, request):
        """恢复实例。此接口的使用场景包括：
         - 读写实例状态为running(运行中)时，批量恢复状态为isolated(已隔离)的只读实例
         - 读写实例状态为isolated(已隔离)时，恢复读写实例
         - 读写实例状态为isolated(已隔离)时，批量恢复读写实例以及状态为isolated(已隔离)的只读实例

        :param request: Request instance for RecoverClusterInstances.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.RecoverClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.RecoverClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewCluster(self, request):
        """续费集群

        :param request: Request instance for RenewCluster.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.RenewClusterRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.RenewClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewCluster", params, headers=headers)
            response = json.loads(body)
            model = models.RenewClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAccountPassword(self, request):
        """重置数据库账号密码

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartClusterInstances(self, request):
        """重启实例，此接口只针对状态为running(运行中)的实例生效。

        :param request: Request instance for RestartClusterInstances.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.RestartClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.RestartClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartClusterInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RestartClusterInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransformClusterPayMode(self, request):
        """转换集群付费模式，目前只支持从 后付费 转换成 与预付费。

        :param request: Request instance for TransformClusterPayMode.
        :type request: :class:`tencentcloud.tdcpg.v20211118.models.TransformClusterPayModeRequest`
        :rtype: :class:`tencentcloud.tdcpg.v20211118.models.TransformClusterPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransformClusterPayMode", params, headers=headers)
            response = json.loads(body)
            model = models.TransformClusterPayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)