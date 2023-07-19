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
from tencentcloud.cfs.v20190719 import models


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.tencentcloudapi.com'
    _service = 'cfs'


    def BindAutoSnapshotPolicy(self, request):
        """文件系统绑定快照策略，可以同时绑定多个fs，一个fs 只能跟一个策略绑定

        :param request: Request instance for BindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.BindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.BindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BindAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoSnapshotPolicy(self, request):
        """创建定期快照策略

        :param request: Request instance for CreateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsFileSystem(self, request):
        """用于添加新文件系统

        :param request: Request instance for CreateCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsPGroup(self, request):
        """本接口（CreateCfsPGroup）用于创建权限组

        :param request: Request instance for CreateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsRule(self, request):
        """本接口（CreateCfsRule）用于创建权限组规则。

        :param request: Request instance for CreateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCfsSnapshot(self, request):
        """创建文件系统快照

        :param request: Request instance for CreateCfsSnapshot.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateCfsSnapshotRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateCfsSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCfsSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCfsSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigrationTask(self, request):
        """用于创建迁移任务。
        此接口需提交工单，开启白名单之后才能使用。

        :param request: Request instance for CreateMigrationTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.CreateMigrationTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.CreateMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoSnapshotPolicy(self, request):
        """删除快照定期策略

        :param request: Request instance for DeleteAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsFileSystem(self, request):
        """用于删除文件系统

        :param request: Request instance for DeleteCfsFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsPGroup(self, request):
        """本接口（DeleteCfsPGroup）用于删除权限组。

        :param request: Request instance for DeleteCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsRule(self, request):
        """本接口（DeleteCfsRule）用于删除权限组规则。

        :param request: Request instance for DeleteCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCfsSnapshot(self, request):
        """删除文件系统快照

        :param request: Request instance for DeleteCfsSnapshot.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsSnapshotRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteCfsSnapshotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCfsSnapshot", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCfsSnapshotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMigrationTask(self, request):
        """用于删除迁移任务。
        此接口需提交工单，开启白名单之后才能使用。

        :param request: Request instance for DeleteMigrationTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteMigrationTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMountTarget(self, request):
        """本接口（DeleteMountTarget）用于删除挂载点

        :param request: Request instance for DeleteMountTarget.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteMountTargetRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteMountTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMountTarget", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMountTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUserQuota(self, request):
        """指定条件删除文件系统配额

        :param request: Request instance for DeleteUserQuota.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DeleteUserQuotaRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DeleteUserQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoSnapshotPolicies(self, request):
        """查询文件系统快照定期策略列表信息

        :param request: Request instance for DescribeAutoSnapshotPolicies.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAutoSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAutoSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAvailableZoneInfo(self, request):
        """本接口（DescribeAvailableZoneInfo）用于查询区域的可用情况。

        :param request: Request instance for DescribeAvailableZoneInfo.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeAvailableZoneInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableZoneInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableZoneInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBucketList(self, request):
        """用于获取数据源桶列表。
        此接口需提交工单，开启白名单之后才能使用。

        :param request: Request instance for DescribeBucketList.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeBucketListRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeBucketListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBucketList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBucketListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsFileSystemClients(self, request):
        """查询挂载该文件系统的客户端。此功能需要客户端安装CFS监控插件。

        :param request: Request instance for DescribeCfsFileSystemClients.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemClientsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsFileSystemClients", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsFileSystemClientsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsFileSystems(self, request):
        """本接口（DescribeCfsFileSystems）用于查询文件系统

        :param request: Request instance for DescribeCfsFileSystems.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsFileSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsFileSystems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsFileSystemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsPGroups(self, request):
        """本接口（DescribeCfsPGroups）用于查询权限组列表。

        :param request: Request instance for DescribeCfsPGroups.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsPGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsPGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsPGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsRules(self, request):
        """本接口（DescribeCfsRules）用于查询权限组规则列表。

        :param request: Request instance for DescribeCfsRules.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsServiceStatus(self, request):
        """本接口（DescribeCfsServiceStatus）用于查询用户使用CFS的服务状态。

        :param request: Request instance for DescribeCfsServiceStatus.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsServiceStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsServiceStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsServiceStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsSnapshotOverview(self, request):
        """文件系统快照概览

        :param request: Request instance for DescribeCfsSnapshotOverview.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotOverviewRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsSnapshotOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsSnapshotOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCfsSnapshots(self, request):
        """查询文件系统快照列表

        :param request: Request instance for DescribeCfsSnapshots.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeCfsSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCfsSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCfsSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationTasks(self, request):
        """用于获取迁移任务列表。
        此接口需提交工单，开启白名单之后才能使用。

        :param request: Request instance for DescribeMigrationTasks.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeMigrationTasksRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeMigrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMountTargets(self, request):
        """本接口（DescribeMountTargets）用于查询文件系统挂载点信息

        :param request: Request instance for DescribeMountTargets.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeMountTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMountTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMountTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotOperationLogs(self, request):
        """查询快照操作日志

        :param request: Request instance for DescribeSnapshotOperationLogs.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeSnapshotOperationLogsRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeSnapshotOperationLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotOperationLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotOperationLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserQuota(self, request):
        """查询文件系统配额（仅部分Turbo实例能使用，若需要调用请提交工单与我们联系）

        :param request: Request instance for DescribeUserQuota.
        :type request: :class:`tencentcloud.cfs.v20190719.models.DescribeUserQuotaRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.DescribeUserQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileSystemAutoScaleUpRule(self, request):
        """用来设置文件系统扩容策略

        :param request: Request instance for ModifyFileSystemAutoScaleUpRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ModifyFileSystemAutoScaleUpRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ModifyFileSystemAutoScaleUpRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileSystemAutoScaleUpRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileSystemAutoScaleUpRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleUpFileSystem(self, request):
        """该接口用于对turbo 文件系统扩容使用

        :param request: Request instance for ScaleUpFileSystem.
        :type request: :class:`tencentcloud.cfs.v20190719.models.ScaleUpFileSystemRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.ScaleUpFileSystemResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpFileSystem", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpFileSystemResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetUserQuota(self, request):
        """设置文件系统配额，提供UID/GID的配额设置的接口

        :param request: Request instance for SetUserQuota.
        :type request: :class:`tencentcloud.cfs.v20190719.models.SetUserQuotaRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.SetUserQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetUserQuota", params, headers=headers)
            response = json.loads(body)
            model = models.SetUserQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SignUpCfsService(self, request):
        """本接口（SignUpCfsService）用于开通CFS服务。

        :param request: Request instance for SignUpCfsService.
        :type request: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.SignUpCfsServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SignUpCfsService", params, headers=headers)
            response = json.loads(body)
            model = models.SignUpCfsServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMigrationTask(self, request):
        """用于终止迁移任务。
        此接口需提交工单，开启白名单之后才能使用。

        :param request: Request instance for StopMigrationTask.
        :type request: :class:`tencentcloud.cfs.v20190719.models.StopMigrationTaskRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.StopMigrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMigrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopMigrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindAutoSnapshotPolicy(self, request):
        """解除文件系统绑定的快照策略

        :param request: Request instance for UnbindAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UnbindAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UnbindAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAutoSnapshotPolicy(self, request):
        """更新定期自动快照策略

        :param request: Request instance for UpdateAutoSnapshotPolicy.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateAutoSnapshotPolicyRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateAutoSnapshotPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAutoSnapshotPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAutoSnapshotPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsFileSystemName(self, request):
        """本接口（UpdateCfsFileSystemName）用于更新文件系统名

        :param request: Request instance for UpdateCfsFileSystemName.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemName", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsFileSystemNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsFileSystemPGroup(self, request):
        """本接口（UpdateCfsFileSystemPGroup）用于更新文件系统所使用的权限组

        :param request: Request instance for UpdateCfsFileSystemPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsFileSystemPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsFileSystemSizeLimit(self, request):
        """本接口（UpdateCfsFileSystemSizeLimit）用于更新文件系统存储容量限制。

        :param request: Request instance for UpdateCfsFileSystemSizeLimit.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsFileSystemSizeLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsFileSystemSizeLimit", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsFileSystemSizeLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsPGroup(self, request):
        """本接口（UpdateCfsPGroup）更新权限组信息。

        :param request: Request instance for UpdateCfsPGroup.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsPGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsPGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsPGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsRule(self, request):
        """本接口（UpdateCfsRule）用于更新权限规则。

        :param request: Request instance for UpdateCfsRule.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsRule", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateCfsSnapshotAttribute(self, request):
        """更新文件系统快照名称及保留时长

        :param request: Request instance for UpdateCfsSnapshotAttribute.
        :type request: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsSnapshotAttributeRequest`
        :rtype: :class:`tencentcloud.cfs.v20190719.models.UpdateCfsSnapshotAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateCfsSnapshotAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateCfsSnapshotAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))