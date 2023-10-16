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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.tencentcloudapi.com'
    _service = 'emr'


    def AddUsersForUserManager(self, request):
        """该接口支持安装了OpenLdap组件的集群。
        新增用户列表（用户管理）。

        :param request: Request instance for AddUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.AddUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """创建EMR集群实例

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateClusterResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstance(self, request):
        """创建EMR集群实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResponse`

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


    def DeleteUserManagerUserList(self, request):
        """删除用户列表（用户管理）

        :param request: Request instance for DeleteUserManagerUserList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DeleteUserManagerUserListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DeleteUserManagerUserListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserManagerUserList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserManagerUserListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoScaleRecords(self, request):
        """获取集群的自动扩缩容的详细记录

        :param request: Request instance for DescribeAutoScaleRecords.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeAutoScaleRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoScaleRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoScaleRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterNodes(self, request):
        """查询集群节点信息

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCvmQuota(self, request):
        """获取账户的CVM配额

        :param request: Request instance for DescribeCvmQuota.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeCvmQuotaRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeCvmQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCvmQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEmrApplicationStatics(self, request):
        """yarn application 统计接口查询

        :param request: Request instance for DescribeEmrApplicationStatics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrApplicationStatics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrApplicationStaticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHiveQueries(self, request):
        """获取hive查询信息

        :param request: Request instance for DescribeHiveQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeHiveQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHiveQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHiveQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImpalaQueries(self, request):
        """DescribeImpalaQueries

        :param request: Request instance for DescribeImpalaQueries.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeImpalaQueriesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeImpalaQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImpalaQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImpalaQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceRenewNodes(self, request):
        """查询待续费节点信息

        :param request: Request instance for DescribeInstanceRenewNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstanceRenewNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstanceRenewNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceRenewNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceRenewNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询集群实例信息

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesList(self, request):
        """查询集群列表

        :param request: Request instance for DescribeInstancesList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobFlow(self, request):
        """查询流程任务

        :param request: Request instance for DescribeJobFlow.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeJobFlowRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeJobFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceSchedule(self, request):
        """查询YARN资源调度数据信息

        :param request: Request instance for DescribeResourceSchedule.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsersForUserManager(self, request):
        """该接口支持安装了OpenLdap组件的集群。
        批量导出用户。对于kerberos集群，如果需要kertab文件下载地址，可以将NeedKeytabInfo设置为true；注意SupportDownLoadKeyTab为true，但是DownLoadKeyTabUrl为空字符串，表示keytab文件在后台没有准备好（正在生成）。

        :param request: Request instance for DescribeUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersForUserManagerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeYarnApplications(self, request):
        """DescribeYarnApplications

        :param request: Request instance for DescribeYarnApplications.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeYarnApplicationsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeYarnApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeYarnApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeYarnApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewEmr(self, request):
        """集群续费询价。

        :param request: Request instance for InquirePriceRenewEmr.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquirePriceRenewEmrRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquirePriceRenewEmrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewEmr", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewEmrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateInstance(self, request):
        """创建实例询价

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewInstance(self, request):
        """续费询价。

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceScaleOutInstance(self, request):
        """扩容询价. 当扩容时候，请通过该接口查询价格。

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpdateInstance(self, request):
        """变配询价

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpdateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpdateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePools(self, request):
        """刷新YARN的动态资源池

        :param request: Request instance for ModifyResourcePools.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcePoolsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePools", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePoolsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduleConfig(self, request):
        """修改YARN资源调度的资源配置

        :param request: Request instance for ModifyResourceScheduleConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceScheduleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceScheduler(self, request):
        """修改了yarn的资源调度器，点击部署生效

        :param request: Request instance for ModifyResourceScheduler.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduler", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceSchedulerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcesTags(self, request):
        """强制修改标签

        :param request: Request instance for ModifyResourcesTags.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcesTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcesTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcesTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserManagerPwd(self, request):
        """修改用户密码（用户管理）

        :param request: Request instance for ModifyUserManagerPwd.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyUserManagerPwdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserManagerPwd", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserManagerPwdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunJobFlow(self, request):
        """创建流程作业

        :param request: Request instance for RunJobFlow.
        :type request: :class:`tencentcloud.emr.v20190103.models.RunJobFlowRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.RunJobFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunJobFlow", params, headers=headers)
            response = json.loads(body)
            model = models.RunJobFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutCluster(self, request):
        """扩容集群节点

        :param request: Request instance for ScaleOutCluster.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        """扩容节点

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartStopServiceOrMonitor(self, request):
        """用于启停服务 重启服务等功能

        :param request: Request instance for StartStopServiceOrMonitor.
        :type request: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.StartStopServiceOrMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartStopServiceOrMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.StartStopServiceOrMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SyncPodState(self, request):
        """EMR同步TKE中POD状态

        :param request: Request instance for SyncPodState.
        :type request: :class:`tencentcloud.emr.v20190103.models.SyncPodStateRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.SyncPodStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncPodState", params, headers=headers)
            response = json.loads(body)
            model = models.SyncPodStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateClusterNodes(self, request):
        """销毁集群节点

        :param request: Request instance for TerminateClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateClusterNodes", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateClusterNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstance(self, request):
        """销毁EMR实例。此接口仅支持弹性MapReduce正式计费版本。

        :param request: Request instance for TerminateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateTasks(self, request):
        """缩容Task节点

        :param request: Request instance for TerminateTasks.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))