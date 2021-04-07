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
            body = self.call("ClearTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CompareIdlFiles(self, request):
        """选中目标表格，上传并校验改表文件，返回是否允许修改表格结构的结果。

        :param request: Request instance for CompareIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CompareIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompareIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompareIdlFilesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBackup(self, request):
        """用户创建备份任务

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCluster(self, request):
        """本接口用于创建TcaplusDB集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSnapshots(self, request):
        """构造表格过去时间点的快照

        :param request: Request instance for CreateSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTableGroup(self, request):
        """在TcaplusDB集群下创建表格组

        :param request: Request instance for CreateTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTableGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTableGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTableGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTables(self, request):
        """根据选择的IDL文件列表，批量创建表格

        :param request: Request instance for CreateTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.CreateTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCluster(self, request):
        """删除TcaplusDB集群，必须在集群所属所有资源（包括表格组，表）都已经释放的情况下才会成功。

        :param request: Request instance for DeleteCluster.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteClusterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCluster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteClusterResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIdlFiles(self, request):
        """指定集群ID和待删除IDL文件的信息，删除目标文件，如果文件正在被表关联则删除失败。

        :param request: Request instance for DeleteIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIdlFilesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSnapshots(self, request):
        """删除表格的快照

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTableGroup(self, request):
        """删除表格组

        :param request: Request instance for DeleteTableGroup.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTableGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTableGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTableIndex(self, request):
        """删除表格的分布式索引

        :param request: Request instance for DeleteTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTableIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTableIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTableIndexResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTables(self, request):
        """删除指定的表,第一次调用此接口代表将表移动至回收站，再次调用代表将此表格从回收站中彻底删除。

        :param request: Request instance for DeleteTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DeleteTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterTags(self, request):
        """获取集群关联的标签列表

        :param request: Request instance for DescribeClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClusterTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusters(self, request):
        """查询TcaplusDB集群列表，包含集群详细信息。

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClustersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIdlFileInfos(self, request):
        """查询表描述文件详情

        :param request: Request instance for DescribeIdlFileInfos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeIdlFileInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIdlFileInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIdlFileInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMachine(self, request):
        """查询独占集群可以申请的剩余机器

        :param request: Request instance for DescribeMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeMachineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMachine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMachineResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRegions(self, request):
        """查询TcaplusDB服务支持的地域列表

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshots(self, request):
        """查询快照列表

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableGroupTags(self, request):
        """获取表格组关联的标签列表

        :param request: Request instance for DescribeTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableGroupTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableGroupTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableGroups(self, request):
        """查询表格组列表

        :param request: Request instance for DescribeTableGroups.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableTags(self, request):
        """获取表格标签

        :param request: Request instance for DescribeTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTableTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTableTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTables(self, request):
        """查询表详情

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTablesInRecycle(self, request):
        """查询回收站中的表详情

        :param request: Request instance for DescribeTablesInRecycle.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTablesInRecycleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTablesInRecycle", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesInRecycleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """查询任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUinInWhitelist(self, request):
        """查询本用户是否在白名单中，控制是否能创建TDR类型的APP或表

        :param request: Request instance for DescribeUinInWhitelist.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DescribeUinInWhitelistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUinInWhitelist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUinInWhitelistResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableRestProxy(self, request):
        """当restful api为关闭状态时，可以通过此接口关闭restful api

        :param request: Request instance for DisableRestProxy.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.DisableRestProxyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.DisableRestProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableRestProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableRestProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableRestProxy(self, request):
        """当restful api为关闭状态时，可以通过此接口开启restful apu

        :param request: Request instance for EnableRestProxy.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.EnableRestProxyRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.EnableRestProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableRestProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableRestProxyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportSnapshots(self, request):
        """将快照数据导入到新表或当前表

        :param request: Request instance for ImportSnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ImportSnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ImportSnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportSnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportSnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterMachine(self, request):
        """修改独占集群机器

        :param request: Request instance for ModifyClusterMachine.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterMachineResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterMachine", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterMachineResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterName(self, request):
        """修改指定的集群名称

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterPassword(self, request):
        """修改指定集群的密码，后台将在旧密码失效之前同时支持TcaplusDB SDK使用旧密码和新密码访问数据库。在旧密码失效之前不能提交新的密码修改请求，在旧密码失效之后不能提交修改旧密码过期时间的请求。

        :param request: Request instance for ModifyClusterPassword.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterPasswordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterTags(self, request):
        """修改集群标签

        :param request: Request instance for ModifyClusterTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyClusterTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyClusterTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySnapshots(self, request):
        """修改表格快照的过期时间

        :param request: Request instance for ModifySnapshots.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifySnapshotsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifySnapshotsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySnapshots", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTableGroupName(self, request):
        """修改TcaplusDB表格组名称

        :param request: Request instance for ModifyTableGroupName.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableGroupName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableGroupNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTableGroupTags(self, request):
        """修改表格组标签

        :param request: Request instance for ModifyTableGroupTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableGroupTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableGroupTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableGroupTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTableMemos(self, request):
        """修改表备注信息

        :param request: Request instance for ModifyTableMemos.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableMemosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableMemos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableMemosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTableQuotas(self, request):
        """表格扩缩容

        :param request: Request instance for ModifyTableQuotas.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableQuotasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableQuotasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTableTags(self, request):
        """修改表格标签

        :param request: Request instance for ModifyTableTags.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTableTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTableTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTableTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTables(self, request):
        """根据用户选定的表定义IDL文件，批量修改指定的表

        :param request: Request instance for ModifyTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.ModifyTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecoverRecycleTables(self, request):
        """恢复回收站中，用户自行删除的表。对欠费待释放的表无效。

        :param request: Request instance for RecoverRecycleTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RecoverRecycleTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecoverRecycleTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecoverRecycleTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RollbackTables(self, request):
        """表格数据回档

        :param request: Request instance for RollbackTables.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.RollbackTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTableIndex(self, request):
        """设置表格分布式索引

        :param request: Request instance for SetTableIndex.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.SetTableIndexResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTableIndex", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTableIndexResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def VerifyIdlFiles(self, request):
        """上传并校验创建表格文件，返回校验合法的表格定义

        :param request: Request instance for VerifyIdlFiles.
        :type request: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesRequest`
        :rtype: :class:`tencentcloud.tcaplusdb.v20190823.models.VerifyIdlFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyIdlFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyIdlFilesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)