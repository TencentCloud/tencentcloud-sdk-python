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
from tencentcloud.cdwdoris.v20211228 import models


class CdwdorisClient(AbstractClient):
    _apiVersion = '2021-12-28'
    _endpoint = 'cdwdoris.tencentcloudapi.com'
    _service = 'cdwdoris'


    def ActionAlterUser(self, request):
        """新增和修改用户接口

        :param request: Request instance for ActionAlterUser.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ActionAlterUserRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ActionAlterUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActionAlterUser", params, headers=headers)
            response = json.loads(body)
            model = models.ActionAlterUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelBackupJob(self, request):
        """取消对应的备份实例任务

        :param request: Request instance for CancelBackupJob.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CancelBackupJobRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CancelBackupJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelBackupJob", params, headers=headers)
            response = json.loads(body)
            model = models.CancelBackupJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCoolDownWorkingVariableConfigCorrect(self, request):
        """查询冷热分层生效变量和配置是否正确

        :param request: Request instance for CheckCoolDownWorkingVariableConfigCorrect.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CheckCoolDownWorkingVariableConfigCorrectRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CheckCoolDownWorkingVariableConfigCorrectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCoolDownWorkingVariableConfigCorrect", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCoolDownWorkingVariableConfigCorrectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackUpSchedule(self, request):
        """创建或者修改备份策略

        :param request: Request instance for CreateBackUpSchedule.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateBackUpScheduleRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateBackUpScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackUpSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackUpScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCoolDownPolicy(self, request):
        """创建冷热分层策略

        :param request: Request instance for CreateCoolDownPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateCoolDownPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateCoolDownPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCoolDownPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCoolDownPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceNew(self, request):
        """通过API创建集群

        :param request: Request instance for CreateInstanceNew.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceNewRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateInstanceNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceNew", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkloadGroup(self, request):
        """创建资源组

        :param request: Request instance for CreateWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.CreateWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.CreateWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackUpData(self, request):
        """删除备份数据

        :param request: Request instance for DeleteBackUpData.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteBackUpDataRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteBackUpDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackUpData", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackUpDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWorkloadGroup(self, request):
        """删除资源组

        :param request: Request instance for DeleteWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DeleteWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAreaRegion(self, request):
        """集群列表页上显示地域信息及各个地域的集群总数

        :param request: Request instance for DescribeAreaRegion.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeAreaRegionRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeAreaRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAreaRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAreaRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpJob(self, request):
        """查询备份实例列表

        :param request: Request instance for DescribeBackUpJob.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpJobDetail(self, request):
        """查询备份任务详情

        :param request: Request instance for DescribeBackUpJobDetail.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobDetailRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpJobDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpJobDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpJobDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpSchedules(self, request):
        """获取备份、迁移的调度任务信息

        :param request: Request instance for DescribeBackUpSchedules.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpSchedulesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpSchedulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpSchedules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpSchedulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpTables(self, request):
        """获取可备份表信息

        :param request: Request instance for DescribeBackUpTables.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTablesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackUpTaskDetail(self, request):
        """查询备份任务进度详情

        :param request: Request instance for DescribeBackUpTaskDetail.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTaskDetailRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeBackUpTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterConfigs(self, request):
        """获取集群的最新的几个配置文件（config.xml、metrika.xml、user.xml）的内容，显示给用户

        :param request: Request instance for DescribeClusterConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterConfigsHistory(self, request):
        """获取集群配置文件修改历史

        :param request: Request instance for DescribeClusterConfigsHistory.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsHistoryRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeClusterConfigsHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterConfigsHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterConfigsHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCoolDownBackends(self, request):
        """查询冷热分层backend节点信息列表

        :param request: Request instance for DescribeCoolDownBackends.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownBackendsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownBackendsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCoolDownBackends", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCoolDownBackendsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCoolDownPolicies(self, request):
        """查询冷热分层策略列表

        :param request: Request instance for DescribeCoolDownPolicies.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownPoliciesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCoolDownPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCoolDownPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCoolDownTableData(self, request):
        """查询冷热分层Table数据

        :param request: Request instance for DescribeCoolDownTableData.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownTableDataRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeCoolDownTableDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCoolDownTableData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCoolDownTableDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseAuditDownload(self, request):
        """下载数据库审计日志

        :param request: Request instance for DescribeDatabaseAuditDownload.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditDownloadRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAuditDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAuditDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseAuditRecords(self, request):
        """获取数据库审计记录

        :param request: Request instance for DescribeDatabaseAuditRecords.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditRecordsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeDatabaseAuditRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseAuditRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseAuditRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        """根据集群ID查询某个集群的具体信息

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        """获取集群节点信息列表

        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodesInfo(self, request):
        """获取BE/FE节点角色

        :param request: Request instance for DescribeInstanceNodesInfo.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesInfoRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodesRole(self, request):
        """获取集群节点角色

        :param request: Request instance for DescribeInstanceNodesRole.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRoleRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceNodesRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodesRole", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceOperations(self, request):
        """在集群详情页面，拉取该集群的操作

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceOperations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceState(self, request):
        """集群详情页中显示集群状态、流程进度等

        :param request: Request instance for DescribeInstanceState.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceStateRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceUsedSubnets(self, request):
        """获取集群已使用子网信息

        :param request: Request instance for DescribeInstanceUsedSubnets.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceUsedSubnetsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstanceUsedSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceUsedSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceUsedSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """获取集群列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesResponse`

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


    def DescribeInstancesHealthState(self, request):
        """集群健康检查

        :param request: Request instance for DescribeInstancesHealthState.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesHealthStateRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeInstancesHealthStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesHealthState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesHealthStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTaskDetail(self, request):
        """查询恢复任务进度详情

        :param request: Request instance for DescribeRestoreTaskDetail.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeRestoreTaskDetailRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeRestoreTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryRecords(self, request):
        """获取慢查询列表

        :param request: Request instance for DescribeSlowQueryRecords.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryRecordsDownload(self, request):
        """下载慢查询文件

        :param request: Request instance for DescribeSlowQueryRecordsDownload.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsDownloadRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSlowQueryRecordsDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryRecordsDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryRecordsDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpec(self, request):
        """购买页拉取集群的数据节点和zookeeper节点的规格列表

        :param request: Request instance for DescribeSpec.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSpecRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSqlApis(self, request):
        """针对驱动sql命令查询集群接口

        :param request: Request instance for DescribeSqlApis.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSqlApisRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeSqlApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSqlApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSqlApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableList(self, request):
        """获取指定数据源和库下的表列表

        :param request: Request instance for DescribeTableList.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeTableListRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeTableListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserBindWorkloadGroup(self, request):
        """获取当前集群各用户绑定的资源信息

        :param request: Request instance for DescribeUserBindWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeUserBindWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeUserBindWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserBindWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserBindWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkloadGroup(self, request):
        """获取资源组信息

        :param request: Request instance for DescribeWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DescribeWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyInstance(self, request):
        """销毁集群

        :param request: Request instance for DestroyInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.DestroyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.DestroyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterConfigs(self, request):
        """在集群配置页面修改集群配置文件接口，xml模式

        :param request: Request instance for ModifyClusterConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCoolDownPolicy(self, request):
        """修改冷热分层策略

        :param request: Request instance for ModifyCoolDownPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyCoolDownPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyCoolDownPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCoolDownPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCoolDownPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        """修改集群名称

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceKeyValConfigs(self, request):
        """KV模式修改配置接口

        :param request: Request instance for ModifyInstanceKeyValConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceKeyValConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyInstanceKeyValConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceKeyValConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceKeyValConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNodeStatus(self, request):
        """修改节点状态

        :param request: Request instance for ModifyNodeStatus.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyNodeStatusRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyNodeStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNodeStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNodeStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroups(self, request):
        """更改安全组

        :param request: Request instance for ModifySecurityGroups.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifySecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifySecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserBindWorkloadGroup(self, request):
        """修改用户绑定的资源组

        :param request: Request instance for ModifyUserBindWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserBindWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserBindWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserBindWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserBindWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserPrivilegesV3(self, request):
        """修改用户权限,支持catalog，全部db，部分db表三种权限设置类别

        :param request: Request instance for ModifyUserPrivilegesV3.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserPrivilegesV3Request`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyUserPrivilegesV3Response`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserPrivilegesV3", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserPrivilegesV3Response()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkloadGroup(self, request):
        """修改资源组信息

        :param request: Request instance for ModifyWorkloadGroup.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkloadGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkloadGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyWorkloadGroupStatus(self, request):
        """开启或关闭资源组

        :param request: Request instance for ModifyWorkloadGroupStatus.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupStatusRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ModifyWorkloadGroupStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkloadGroupStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkloadGroupStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenCoolDown(self, request):
        """开始启用冷热分层

        :param request: Request instance for OpenCoolDown.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenCoolDown", params, headers=headers)
            response = json.loads(body)
            model = models.OpenCoolDownResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenCoolDownPolicy(self, request):
        """开通、描述降冷策略接口

        :param request: Request instance for OpenCoolDownPolicy.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownPolicyRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.OpenCoolDownPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenCoolDownPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.OpenCoolDownPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverBackUpJob(self, request):
        """备份恢复

        :param request: Request instance for RecoverBackUpJob.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RecoverBackUpJobRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RecoverBackUpJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverBackUpJob", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverBackUpJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReduceInstance(self, request):
        """集群缩容

        :param request: Request instance for ReduceInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ReduceInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ReduceInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReduceInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ReduceInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResizeDisk(self, request):
        """扩容云盘

        :param request: Request instance for ResizeDisk.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ResizeDiskRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDisk", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartClusterForConfigs(self, request):
        """重启集群让配置文件生效

        :param request: Request instance for RestartClusterForConfigs.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForConfigsRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartClusterForConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.RestartClusterForConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartClusterForNode(self, request):
        """集群滚动重启

        :param request: Request instance for RestartClusterForNode.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForNodeRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.RestartClusterForNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartClusterForNode", params, headers=headers)
            response = json.loads(body)
            model = models.RestartClusterForNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        """水平扩容节点

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleOutInstanceResponse`

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


    def ScaleUpInstance(self, request):
        """计算资源垂直变配

        :param request: Request instance for ScaleUpInstance.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleUpInstanceRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.ScaleUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCoolDown(self, request):
        """更新集群冷热分层信息

        :param request: Request instance for UpdateCoolDown.
        :type request: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateCoolDownRequest`
        :rtype: :class:`tencentcloud.cdwdoris.v20211228.models.UpdateCoolDownResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCoolDown", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCoolDownResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))