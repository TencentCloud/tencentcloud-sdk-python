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
from tencentcloud.tcaplusdb.v20190823 import models


class TcaplusdbClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tcaplusdb.tencentcloudapi.com'
    _service = 'tcaplusdb'


    def ClearTables(self, request):
        """根据给定的表信息，清除表数据。

        :param request: Request instance for ClearTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ClearTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ClearTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearTables", params, headers=headers)
            response = json.loads(body)
            model = models.ClearTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompareIdlFiles(self, request):
        """选中目标表格，上传并校验改表文件，返回是否允许修改表格结构的结果。

        :param request: Request instance for CompareIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompareIdlFiles", params, headers=headers)
            response = json.loads(body)
            model = models.CompareIdlFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        """用户创建备份任务

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCluster(self, request):
        """本接口用于创建TcaplusDB集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterResponse`

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


    def CreateSnapshots(self, request):
        """构造表格过去时间点的快照

        :param request: Request instance for CreateSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTableGroup(self, request):
        """在TcaplusDB集群下创建表格组

        :param request: Request instance for CreateTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTableGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTableGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTables(self, request):
        """根据选择的IDL文件列表，批量创建表格

        :param request: Request instance for CreateTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTables", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupRecords(self, request):
        """删除手工备份

        :param request: Request instance for DeleteBackupRecords.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteBackupRecordsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteBackupRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCluster(self, request):
        """删除TcaplusDB集群，必须在集群所属所有资源（包括表格组，表）都已经释放的情况下才会成功。

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIdlFiles(self, request):
        """指定集群ID和待删除IDL文件的信息，删除目标文件，如果文件正在被表关联则删除失败。

        :param request: Request instance for DeleteIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIdlFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIdlFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshots(self, request):
        """删除表格的快照

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTableDataFlow(self, request):
        """删除表格的数据订阅

        :param request: Request instance for DeleteTableDataFlow.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableDataFlowRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTableGroup(self, request):
        """删除表格组

        :param request: Request instance for DeleteTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTableIndex(self, request):
        """删除表格的分布式索引

        :param request: Request instance for DeleteTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableIndex", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTables(self, request):
        """删除指定的表,第一次调用此接口代表将表移动至回收站，再次调用代表将此表格从回收站中彻底删除。

        :param request: Request instance for DeleteTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeApplications(self, request):
        """获取审批管理的申请单

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupRecords(self, request):
        """查询备份记录

        查询集群级别时， 将TableGroupId设置为"-1", 将TableName设置为"-1"
        查询集群+表格组级别时， 将TableName设置为"-1"
        查询集群+表格组+表格级别时， 都不能设置为“-1”

        :param request: Request instance for DescribeBackupRecords.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeBackupRecordsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeBackupRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterTags(self, request):
        """获取集群关联的标签列表

        :param request: Request instance for DescribeClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """查询TcaplusDB集群列表，包含集群详细信息。

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIdlFileInfos(self, request):
        """查询表描述文件详情

        :param request: Request instance for DescribeIdlFileInfos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIdlFileInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIdlFileInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMachine(self, request):
        """查询独占集群可以申请的剩余机器

        :param request: Request instance for DescribeMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMachine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """查询TcaplusDB服务支持的地域列表

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshots(self, request):
        """查询快照列表

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableGroupTags(self, request):
        """获取表格组关联的标签列表

        :param request: Request instance for DescribeTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableGroupTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableGroupTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableGroups(self, request):
        """查询表格组列表

        :param request: Request instance for DescribeTableGroups.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTableTags(self, request):
        """获取表格标签

        :param request: Request instance for DescribeTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        """查询表详情

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTablesInRecycle(self, request):
        """查询回收站中的表详情

        :param request: Request instance for DescribeTablesInRecycle.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablesInRecycle", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesInRecycleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """查询任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUinInWhitelist(self, request):
        """查询本用户是否在白名单中，控制是否能创建TDR类型的APP或表

        :param request: Request instance for DescribeUinInWhitelist.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUinInWhitelist", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUinInWhitelistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRestProxy(self, request):
        """当restful api为关闭状态时，可以通过此接口关闭restful api

        :param request: Request instance for DisableRestProxy.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DisableRestProxyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DisableRestProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRestProxy", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRestProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableRestProxy(self, request):
        """当restful api为关闭状态时，可以通过此接口开启restful api。

        :param request: Request instance for EnableRestProxy.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.EnableRestProxyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.EnableRestProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableRestProxy", params, headers=headers)
            response = json.loads(body)
            model = models.EnableRestProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportSnapshots(self, request):
        """将快照数据导入到新表或当前表

        :param request: Request instance for ImportSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ImportSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ImportSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.ImportSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MergeTablesData(self, request):
        """合并指定表格

        :param request: Request instance for MergeTablesData.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.MergeTablesDataRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.MergeTablesDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MergeTablesData", params, headers=headers)
            response = json.loads(body)
            model = models.MergeTablesDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCensorship(self, request):
        """修改集群审批状态

        :param request: Request instance for ModifyCensorship.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyCensorshipRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyCensorshipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCensorship", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCensorshipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterMachine(self, request):
        """修改独占集群机器

        :param request: Request instance for ModifyClusterMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterMachine", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterMachineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterName(self, request):
        """修改指定的集群名称

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterPassword(self, request):
        """修改指定集群的密码，后台将在旧密码失效之前同时支持TcaplusDB SDK使用旧密码和新密码访问数据库。在旧密码失效之前不能提交新的密码修改请求，在旧密码失效之后不能提交修改旧密码过期时间的请求。

        :param request: Request instance for ModifyClusterPassword.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterTags(self, request):
        """修改集群标签

        :param request: Request instance for ModifyClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshots(self, request):
        """修改表格快照的过期时间

        :param request: Request instance for ModifySnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifySnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifySnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableGroupName(self, request):
        """修改TcaplusDB表格组名称

        :param request: Request instance for ModifyTableGroupName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableGroupName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableGroupNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableGroupTags(self, request):
        """修改表格组标签

        :param request: Request instance for ModifyTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableGroupTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableGroupTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableMemos(self, request):
        """修改表备注信息

        :param request: Request instance for ModifyTableMemos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableMemos", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableMemosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableQuotas(self, request):
        """表格扩缩容

        :param request: Request instance for ModifyTableQuotas.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTableTags(self, request):
        """修改表格标签

        :param request: Request instance for ModifyTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTableTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTableTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTables(self, request):
        """根据用户选定的表定义IDL文件，批量修改指定的表

        :param request: Request instance for ModifyTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTables", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecoverRecycleTables(self, request):
        """恢复回收站中，用户自行删除的表。对欠费待释放的表无效。

        :param request: Request instance for RecoverRecycleTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecoverRecycleTables", params, headers=headers)
            response = json.loads(body)
            model = models.RecoverRecycleTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackTables(self, request):
        """表格数据回档

        :param request: Request instance for RollbackTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackTables", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBackupExpireRule(self, request):
        """新增、删除、修改备份过期策略， ClusterId必须为具体的集群Id（appid）

        :param request: Request instance for SetBackupExpireRule.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetBackupExpireRuleRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetBackupExpireRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBackupExpireRule", params, headers=headers)
            response = json.loads(body)
            model = models.SetBackupExpireRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTableDataFlow(self, request):
        """新增、修改表格数据订阅

        :param request: Request instance for SetTableDataFlow.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableDataFlowRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableDataFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTableDataFlow", params, headers=headers)
            response = json.loads(body)
            model = models.SetTableDataFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetTableIndex(self, request):
        """设置表格分布式索引

        :param request: Request instance for SetTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTableIndex", params, headers=headers)
            response = json.loads(body)
            model = models.SetTableIndexResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateApply(self, request):
        """更新申请单状态

        :param request: Request instance for UpdateApply.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.UpdateApplyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.UpdateApplyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApply", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApplyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyIdlFiles(self, request):
        """上传并校验创建表格文件，返回校验合法的表格定义

        :param request: Request instance for VerifyIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyIdlFiles", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyIdlFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))