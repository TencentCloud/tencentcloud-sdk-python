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
from tencentcloud.cynosdb.v20190107 import models


class CynosdbClient(AbstractClient):
    _apiVersion = '2019-01-07'
    _endpoint = 'cynosdb.tencentcloudapi.com'
    _service = 'cynosdb'


    def ActivateInstance(self, request):
        """本接口(ActivateInstance)用于恢复已隔离的实例访问。

        :param request: Request instance for ActivateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ActivateInstanceResponse()
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


    def AddClusterSlaveZone(self, request):
        """增加从可用区

        :param request: Request instance for AddClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddClusterSlaveZoneResponse()
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


    def AddInstances(self, request):
        """本接口（AddInstances）用于集群添加实例

        :param request: Request instance for AddInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddInstancesResponse()
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


    def AssociateSecurityGroups(self, request):
        """安全组批量绑定云资源

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
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


    def CreateAccounts(self, request):
        """创建账号

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccounts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountsResponse()
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
        """为集群创建手动备份

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
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


    def CreateClusters(self, request):
        """创建集群

        :param request: Request instance for CreateClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusters", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateClustersResponse()
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


    def DescribeAccountAllGrantPrivileges(self, request):
        """账号所有权限

        :param request: Request instance for DescribeAccountAllGrantPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountAllGrantPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountAllGrantPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountAllGrantPrivileges", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountAllGrantPrivilegesResponse()
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


    def DescribeAccounts(self, request):
        """本接口(DescribeAccounts)用于查询数据库管理账号。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeBackupConfig(self, request):
        """获取指定集群的备份配置信息，包括全量备份时间段，备份文件保留时间

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupConfigResponse()
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


    def DescribeBackupDownloadUrl(self, request):
        """此接口（DescribeBackupDownloadUrl）用于查询集群备份文件下载地址。

        :param request: Request instance for DescribeBackupDownloadUrl.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupDownloadUrlResponse()
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


    def DescribeBackupList(self, request):
        """查询备份文件列表

        :param request: Request instance for DescribeBackupList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupListResponse()
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


    def DescribeBinlogDownloadUrl(self, request):
        """此接口（DescribeBinlogDownloadUrl）用于查询Binlog的下载地址。

        :param request: Request instance for DescribeBinlogDownloadUrl.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogDownloadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBinlogDownloadUrlResponse()
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


    def DescribeBinlogSaveDays(self, request):
        """此接口（DescribeBinlogSaveDays）用于查询集群的Binlog保留天数。

        :param request: Request instance for DescribeBinlogSaveDays.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogSaveDaysRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogSaveDaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogSaveDays", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBinlogSaveDaysResponse()
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


    def DescribeBinlogs(self, request):
        """此接口（DescribeBinlogs）用来查询集群Binlog日志列表。

        :param request: Request instance for DescribeBinlogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBinlogsResponse()
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


    def DescribeClusterDetail(self, request):
        """显示集群详情

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterDetailResponse()
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


    def DescribeClusterInstanceGrps(self, request):
        """本接口（DescribeClusterInstanceGrps）用于查询实例组

        :param request: Request instance for DescribeClusterInstanceGrps.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstanceGrps", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstanceGrpsResponse()
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


    def DescribeClusterParamLogs(self, request):
        """本接口（DescribeClusterParamLogs）查询参数修改日志

        :param request: Request instance for DescribeClusterParamLogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterParamLogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterParamLogsResponse()
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


    def DescribeClusterParams(self, request):
        """本接口（DescribeClusterParams）用于查询集群参数

        :param request: Request instance for DescribeClusterParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterParams", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterParamsResponse()
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
        """查询集群列表

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
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


    def DescribeDBSecurityGroups(self, request):
        """查询实例安全组信息

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
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


    def DescribeInstanceDetail(self, request):
        """本接口(DescribeInstanceDetail)用于查询实例详情。

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDetailResponse()
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


    def DescribeInstanceSlowQueries(self, request):
        """此接口（DescribeInstanceSlowQueries）用于查询实例慢查询日志。

        :param request: Request instance for DescribeInstanceSlowQueries.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSlowQueriesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSlowQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSlowQueries", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceSlowQueriesResponse()
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


    def DescribeInstanceSpecs(self, request):
        """本接口（DescribeInstanceSpecs）用于查询实例规格

        :param request: Request instance for DescribeInstanceSpecs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSpecs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceSpecsResponse()
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


    def DescribeInstances(self, request):
        """本接口(DescribeInstances)用于查询实例列表。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
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


    def DescribeMaintainPeriod(self, request):
        """查询实例维护时间窗

        :param request: Request instance for DescribeMaintainPeriod.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintainPeriod", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaintainPeriodResponse()
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


    def DescribeParamTemplates(self, request):
        """查询用户指定产品下的所有参数模板信息

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplates", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeParamTemplatesResponse()
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


    def DescribeProjectSecurityGroups(self, request):
        """查询项目安全组信息

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
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


    def DescribeResourcesByDealName(self, request):
        """根据计费订单id查询资源列表

        :param request: Request instance for DescribeResourcesByDealName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByDealName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByDealNameResponse()
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


    def DescribeRollbackTimeRange(self, request):
        """查询指定集群有效回滚时间范围

        :param request: Request instance for DescribeRollbackTimeRange.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeRange", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackTimeRangeResponse()
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


    def DescribeRollbackTimeValidity(self, request):
        """指定时间和集群查询是否可回滚

        :param request: Request instance for DescribeRollbackTimeValidity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeValidity", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackTimeValidityResponse()
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


    def DisassociateSecurityGroups(self, request):
        """安全组批量解绑云资源

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
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


    def ExportInstanceSlowQueries(self, request):
        """此接口（ExportInstanceSlowQueries）用于导出实例慢日志。

        :param request: Request instance for ExportInstanceSlowQueries.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceSlowQueriesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceSlowQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportInstanceSlowQueries", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExportInstanceSlowQueriesResponse()
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


    def GrantAccountPrivileges(self, request):
        """批量授权账号权限

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantAccountPrivilegesResponse()
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


    def InquirePriceCreate(self, request):
        """查询新购集群价格

        :param request: Request instance for InquirePriceCreate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceCreateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceCreateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreate", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceCreateResponse()
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


    def InquirePriceRenew(self, request):
        """查询续费集群价格

        :param request: Request instance for InquirePriceRenew.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceRenewRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceRenewResponse()
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


    def IsolateCluster(self, request):
        """隔离集群

        :param request: Request instance for IsolateCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateClusterResponse()
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


    def IsolateInstance(self, request):
        """本接口(IsolateInstance)用于隔离实例。

        :param request: Request instance for IsolateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateInstanceResponse()
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


    def ModifyAccountParams(self, request):
        """修改账号参数

        :param request: Request instance for ModifyAccountParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountParams", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountParamsResponse()
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


    def ModifyBackupConfig(self, request):
        """修改指定集群的备份配置

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupConfigResponse()
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


    def ModifyBackupName(self, request):
        """此接口（ModifyBackupName）用于修改备份文件备注名。

        :param request: Request instance for ModifyBackupName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupNameResponse()
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
        """修改集群名称

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterName", params, headers=headers)
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


    def ModifyClusterParam(self, request):
        """修改集群参数

        :param request: Request instance for ModifyClusterParam.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterParam", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterParamResponse()
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


    def ModifyClusterSlaveZone(self, request):
        """修改从可用区

        :param request: Request instance for ModifyClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterSlaveZoneResponse()
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


    def ModifyClusterStorage(self, request):
        """升级预付费存储

        :param request: Request instance for ModifyClusterStorage.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterStorageRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterStorage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyClusterStorageResponse()
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


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
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


    def ModifyInstanceName(self, request):
        """本接口(ModifyInstanceName)用于修改实例名称。

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceNameResponse()
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


    def ModifyMaintainPeriodConfig(self, request):
        """修改维护时间配置

        :param request: Request instance for ModifyMaintainPeriodConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintainPeriodConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMaintainPeriodConfigResponse()
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


    def OfflineCluster(self, request):
        """下线集群

        :param request: Request instance for OfflineCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineClusterResponse()
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


    def OfflineInstance(self, request):
        """下线实例

        :param request: Request instance for OfflineInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineInstanceResponse()
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


    def PauseServerless(self, request):
        """暂停serverless集群

        :param request: Request instance for PauseServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseServerless", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PauseServerlessResponse()
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


    def RemoveClusterSlaveZone(self, request):
        """删除从可用区

        :param request: Request instance for RemoveClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RemoveClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RemoveClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveClusterSlaveZoneResponse()
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


    def ResumeServerless(self, request):
        """恢复serverless集群

        :param request: Request instance for ResumeServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeServerless", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeServerlessResponse()
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


    def RevokeAccountPrivileges(self, request):
        """批量回收账号权限

        :param request: Request instance for RevokeAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RevokeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RevokeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevokeAccountPrivilegesResponse()
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


    def RollBackCluster(self, request):
        """本接口（RollBackCluster）用于回档集群

        :param request: Request instance for RollBackCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RollBackClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RollBackClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollBackCluster", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollBackClusterResponse()
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


    def SetRenewFlag(self, request):
        """SetRenewFlag设置实例的自动续费功能

        :param request: Request instance for SetRenewFlag.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRenewFlag", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetRenewFlagResponse()
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


    def SwitchClusterZone(self, request):
        """切换到从可用区

        :param request: Request instance for SwitchClusterZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchClusterZone", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchClusterZoneResponse()
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


    def UpgradeInstance(self, request):
        """升级实例

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceResponse()
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