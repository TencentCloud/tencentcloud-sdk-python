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
from tencentcloud.mongodb.v20190725 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2019-07-25'
    _endpoint = 'mongodb.tencentcloudapi.com'
    _service = 'mongodb'


    def AssignProject(self, request):
        r"""本接口(AssignProject)用于指定云数据库实例的所属项目。

        :param request: Request instance for AssignProject.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignProject", params, headers=headers)
            response = json.loads(body)
            model = models.AssignProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccountUser(self, request):
        r"""本接口（CreateAccountUser）用于自定义实例访问账号。

        :param request: Request instance for CreateAccountUser.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateAccountUserRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateAccountUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccountUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditLogFile(self, request):
        r"""本接口(CreateAuditLogFile)用于创建云数据库实例的审计日志文件。

        :param request: Request instance for CreateAuditLogFile.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateAuditLogFileRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupDBInstance(self, request):
        r"""本接口（CreateBackupDBInstance）用于备份实例。

        :param request: Request instance for CreateBackupDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupDownloadTask(self, request):
        r"""本接口用来创建某个备份文件的下载任务

        :param request: Request instance for CreateBackupDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateBackupDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstance(self, request):
        r"""本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。接口支持的售卖规格，可通过接口查询 [DescribeSpecInfo](https://cloud.tencent.com/document/product/240/35767) 获取。

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstanceHour(self, request):
        r"""本接口（CreateDBInstanceHour）用于创建按量计费的MongoDB云数据库实例。

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceHour", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceHourResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstanceParamTpl(self, request):
        r"""本接口(CreateDBInstanceParamTpl)用于创建云数据库MongoDB实例的参数模板
        **说明：CreateDBInstanceParamTpl API正在公测中，在此期间，该接口仅对公测用户开放**

        :param request: Request instance for CreateDBInstanceParamTpl.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceParamTplRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateDBInstanceParamTplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceParamTpl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceParamTplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLogDownloadTask(self, request):
        r"""创建日志下载任务

        :param request: Request instance for CreateLogDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.CreateLogDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.CreateLogDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLogDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccountUser(self, request):
        r"""本接口（DeleteAccountUser）用于删除实例的自定义账号。

        :param request: Request instance for DeleteAccountUser.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DeleteAccountUserRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DeleteAccountUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccountUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditLogFile(self, request):
        r"""本接口(DeleteAuditLogFile)用于删除云数据库实例的审计日志文件。

        :param request: Request instance for DeleteAuditLogFile.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DeleteAuditLogFileRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DeleteAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogDownloadTask(self, request):
        r"""删除日志下载任务

        :param request: Request instance for DeleteLogDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DeleteLogDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DeleteLogDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountUsers(self, request):
        r"""本接口（DescribeAccountUsers）用于获取当前实例的全部账号。

        :param request: Request instance for DescribeAccountUsers.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeAccountUsersRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeAccountUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsyncRequestInfo(self, request):
        r"""本接口（DescribeAsyncRequestInfo）用于查询异步任务状态接口。

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncRequestInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncRequestInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditInstanceList(self, request):
        r"""本接口（DescribeAuditInstanceList）用于查询开通或未开通数据库审计的实例列表。

        :param request: Request instance for DescribeAuditInstanceList.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeAuditInstanceListRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeAuditInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadTask(self, request):
        r"""本接口（DescribeBackupDownloadTask）用于查询备份下载任务信息。

        :param request: Request instance for DescribeBackupDownloadTask.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupDownloadTaskRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupDownloadTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupRules(self, request):
        r"""本接口（DescribeBackupRules）用于获取实例自动备份配置信息。

        :param request: Request instance for DescribeBackupRules.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupRulesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeBackupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientConnections(self, request):
        r"""本接口（DescribeClientConnections）用于查询实例客户端连接信息，包括连接 IP 和连接数量。

        :param request: Request instance for DescribeClientConnections.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeClientConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCurrentOp(self, request):
        r"""本接口（DescribeCurrentOp）用于查询云数据库实例的当前正在执行的操作。

        :param request: Request instance for DescribeCurrentOp.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeCurrentOpRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeCurrentOpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCurrentOp", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCurrentOpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBBackups(self, request):
        r"""本接口（DescribeDBBackups）用于查询实例备份列表，目前只支持查询7天内的备份记录。

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceDeal(self, request):
        r"""本接口（DescribeDBInstanceDeal）用于获取MongoDB购买、续费及变配订单详细。

        :param request: Request instance for DescribeDBInstanceDeal.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceDealResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceDeal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceDealResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceNamespace(self, request):
        r"""本接口（DescribeDBInstanceNamespace）用于查询数据库的表信息。

        :param request: Request instance for DescribeDBInstanceNamespace.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNamespaceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNamespaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceNamespace", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceNamespaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceNodeProperty(self, request):
        r"""本接口用于查询节点的属性，包括节点所在可用区、节点名称、地址、角色、状态、主从延迟、优先级、投票权、标签等属性。

        :param request: Request instance for DescribeDBInstanceNodeProperty.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNodePropertyRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceNodePropertyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceNodeProperty", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceNodePropertyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceParamTpl(self, request):
        r"""本接口(DescribeDBInstanceParamTpl )用于查询当前账号下所有MongoDB数据库参数模板
        **说明：DescribeDBInstanceParamTpl  API正在公测中，在此期间，该接口仅对公测用户开放**

        :param request: Request instance for DescribeDBInstanceParamTpl.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceParamTplRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceParamTplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceParamTpl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceParamTplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceParamTplDetail(self, request):
        r"""本接口(DescribeDBInstanceParamTplDetail )用于查询MongoDB云数据库实例的参数模板详情。
        **说明：DescribeDBInstanceParamTplDetail  API正在公测中，在此期间，该接口仅对公测用户开放**

        :param request: Request instance for DescribeDBInstanceParamTplDetail.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceParamTplDetailRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceParamTplDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceParamTplDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceParamTplDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceURL(self, request):
        r"""本接口（DescribeDBInstanceURL）用于获取指定实例的 URI 形式的连接串访问地址示例。

        :param request: Request instance for DescribeDBInstanceURL.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceURLRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstanceURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        r"""本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选主实例、灾备实例和只读实例信息列表。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDetailedSlowLogs(self, request):
        r"""本接口（DescribeDetailedSlowLogs）用于查询实例慢日志详情。

        :param request: Request instance for DescribeDetailedSlowLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeDetailedSlowLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeDetailedSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDetailedSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDetailedSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        r"""本接口（DescribeInstanceParams）用于查询当前实例可修改的参数列表。

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogDownloadTasks(self, request):
        r"""日志下载任务查询

        :param request: Request instance for DescribeLogDownloadTasks.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeLogDownloadTasksRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeLogDownloadTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogDownloadTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogDownloadTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMongodbLogs(self, request):
        r"""该接口（DescribeMongodbLogs）用于查询运行日志。

        :param request: Request instance for DescribeMongodbLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeMongodbLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeMongodbLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMongodbLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMongodbLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroup(self, request):
        r"""本接口（DescribeSecurityGroup）用于查询实例绑定的安全组。

        :param request: Request instance for DescribeSecurityGroup.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogPatterns(self, request):
        r"""本接口（DescribeSlowLogPatterns）用于获取数据库实例慢日志的统计信息。

        :param request: Request instance for DescribeSlowLogPatterns.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogPatternsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogPatterns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogPatternsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogs(self, request):
        r"""本接口（DescribeSlowLogs）用于获取云数据库慢日志信息。接口只支持查询最近7天内慢日志。

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecInfo(self, request):
        r"""本接口（DescribeSpecInfo）用于查询实例的售卖规格。

        :param request: Request instance for DescribeSpecInfo.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTransparentDataEncryptionStatus(self, request):
        r"""获取实例透明加密的开启状态

        :param request: Request instance for DescribeTransparentDataEncryptionStatus.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DescribeTransparentDataEncryptionStatusRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DescribeTransparentDataEncryptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTransparentDataEncryptionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTransparentDataEncryptionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DropDBInstanceParamTpl(self, request):
        r"""本接口(DropDBInstanceParamTpl )用于删除云数据库MongoDB实例的参数模板
        **说明：DropDBInstanceParamTpl  API正在公测中，在此期间，该接口仅对公测用户开放**

        :param request: Request instance for DropDBInstanceParamTpl.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.DropDBInstanceParamTplRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.DropDBInstanceParamTplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDBInstanceParamTpl", params, headers=headers)
            response = json.loads(body)
            model = models.DropDBInstanceParamTplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableTransparentDataEncryption(self, request):
        r"""本接口（EnableTransparentDataEncryption）用于开启云数据库 MongoDB 的透明加密能力。

        :param request: Request instance for EnableTransparentDataEncryption.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.EnableTransparentDataEncryptionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.EnableTransparentDataEncryptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableTransparentDataEncryption", params, headers=headers)
            response = json.loads(body)
            model = models.EnableTransparentDataEncryptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FlashBackDBInstance(self, request):
        r"""该接口用于发起按 Key 闪回任务，依据数据的闪回 Key（默认为 id）对数据进行极速回档，快速恢复业务。
        **说明：按 Key 闪回于2023年09月11日正式进行公测，在此期间，该接口仅对公测用户开放。**

        :param request: Request instance for FlashBackDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.FlashBackDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.FlashBackDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FlashBackDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.FlashBackDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FlushInstanceRouterConfig(self, request):
        r"""在所有mongos上执行FlushRouterConfig命令

        :param request: Request instance for FlushInstanceRouterConfig.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.FlushInstanceRouterConfigRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.FlushInstanceRouterConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FlushInstanceRouterConfig", params, headers=headers)
            response = json.loads(body)
            model = models.FlushInstanceRouterConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateDBInstances(self, request):
        r"""本接口（InquirePriceCreateDBInstances）用于创建数据库实例询价。本接口参数中必须传入region参数，否则无法通过校验。本接口仅允许针对购买限制范围内的实例配置进行询价。

        :param request: Request instance for InquirePriceCreateDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceModifyDBInstanceSpec(self, request):
        r"""本接口 (InquirePriceModifyDBInstanceSpec) 用于查询实例配置变更后的价格。

        :param request: Request instance for InquirePriceModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceModifyDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceModifyDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenewDBInstances(self, request):
        r"""本接口 (InquiryPriceRenewDBInstances) 用于续费包年包月实例询价。

        :param request: Request instance for InquirePriceRenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.InquirePriceRenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDBInstance(self, request):
        r"""本接口（IsolateDBInstance）用于隔离 MongoDB 云数据库按量计费实例。隔离后实例保留在回收站中，不能再写入数据。隔离一定时间后，实例会彻底删除，回收站保存时间请参考按量计费的服务条款。已删除的按量计费实例无法恢复，请谨慎操作。

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillOps(self, request):
        r"""本接口（KillOps）用于终止 MongoDB 云数据库实例上执行的特定操作。

        :param request: Request instance for KillOps.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.KillOpsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.KillOpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillOps", params, headers=headers)
            response = json.loads(body)
            model = models.KillOpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditService(self, request):
        r"""本接口(ModifyAuditService)用于修改云数据库审计策略的服务配置，包括审计日志保存时长等。

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceNetworkAddress(self, request):
        r"""本接口（ModifyDBInstanceNetworkAddress）用于修改云数据库实例的网络信息，支持基础网络切换为私有网络、私有网络切换私有网络。

        :param request: Request instance for ModifyDBInstanceNetworkAddress.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceNetworkAddressRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceNetworkAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceNetworkAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNetworkAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceParamTpl(self, request):
        r"""本接口(ModifyDBInstanceParamTpl )用于修改MongoDB云数据库实例的参数模板。
        **说明：ModifyDBInstanceParamTpl  API正在公测中，在此期间，该接口仅对公测用户开放**

        :param request: Request instance for ModifyDBInstanceParamTpl.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceParamTplRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceParamTplResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceParamTpl", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceParamTplResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroup(self, request):
        r"""本接口（ModifyDBInstanceSecurityGroup）用于修改实例绑定的安全组

        :param request: Request instance for ModifyDBInstanceSecurityGroup.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSecurityGroupRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSpec(self, request):
        r"""本接口（ModifyDBInstanceSpec）用于调整MongoDB云数据库实例配置。接口支持的售卖规格，可从查询云数据库的售卖规格（[DescribeSpecInfo](https://cloud.tencent.com/document/product/240/38567)）获取。

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParams(self, request):
        r"""本接口（ModifyInstanceParams）用于修改mongoDB实例的参数配置。

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ModifyInstanceParamsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineIsolatedDBInstance(self, request):
        r"""本接口(OfflineIsolatedDBInstance)用于立即下线隔离状态的云数据库实例。进行操作的实例状态必须为隔离状态。

        :param request: Request instance for OfflineIsolatedDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.OfflineIsolatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineIsolatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineIsolatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        r"""本接口(OpenAuditService)用于开通云数据库实例的审计。

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.OpenAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameInstance(self, request):
        r"""本接口(RenameInstance)用于修改云数据库实例的名称。

        :param request: Request instance for RenameInstance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenameInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDBInstances(self, request):
        r"""本接口(RenewDBInstance)用于续费云数据库实例，仅支持付费模式为包年包月的实例。按量计费实例不需要续费。

        :param request: Request instance for RenewDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RenewDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetDBInstancePassword(self, request):
        r"""本接口（ResetDBInstancePassword）用于重置实例访问密码。

        :param request: Request instance for ResetDBInstancePassword.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.ResetDBInstancePasswordRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.ResetDBInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetDBInstancePassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetDBInstancePasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartNodes(self, request):
        r"""本接口（RestartNodes）用于批量重启数据库节点。

        :param request: Request instance for RestartNodes.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.RestartNodesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.RestartNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartNodes", params, headers=headers)
            response = json.loads(body)
            model = models.RestartNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAccountUserPrivilege(self, request):
        r"""本接口（SetAccountUserPrivilege）用于设置实例的账号权限。

        :param request: Request instance for SetAccountUserPrivilege.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetAccountUserPrivilegeRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetAccountUserPrivilegeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAccountUserPrivilege", params, headers=headers)
            response = json.loads(body)
            model = models.SetAccountUserPrivilegeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetBackupRules(self, request):
        r"""本接口(SetBackupRules)用于设置 MongoDB 云数据库的自动备份规则。

        :param request: Request instance for SetBackupRules.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetBackupRulesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetBackupRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetBackupRules", params, headers=headers)
            response = json.loads(body)
            model = models.SetBackupRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetDBInstanceDeletionProtection(self, request):
        r"""本接口（SetDBInstanceDeletionProtection）用于设置实例销毁保护

        :param request: Request instance for SetDBInstanceDeletionProtection.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetDBInstanceDeletionProtectionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetDBInstanceDeletionProtectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetDBInstanceDeletionProtection", params, headers=headers)
            response = json.loads(body)
            model = models.SetDBInstanceDeletionProtectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetInstanceMaintenance(self, request):
        r"""本接口（SetInstanceMaintenance ） 用于设置实例维护时间窗。

        :param request: Request instance for SetInstanceMaintenance.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.SetInstanceMaintenanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.SetInstanceMaintenanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetInstanceMaintenance", params, headers=headers)
            response = json.loads(body)
            model = models.SetInstanceMaintenanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDBInstances(self, request):
        r"""本接口（TerminateDBInstances）用于退还包年包月计费实例。

        :param request: Request instance for TerminateDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.TerminateDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.TerminateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstanceKernelVersion(self, request):
        r"""本接口(UpgradeDBInstanceKernelVersion)用于升级数据库实例内核版本。

        :param request: Request instance for UpgradeDBInstanceKernelVersion.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDBInstanceKernelVersionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDBInstanceKernelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceKernelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceKernelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDbInstanceVersion(self, request):
        r"""本接口用于跨版本升级数据库内核。当前仅支持3.6版本升级为4.0版本、4.0版本升级为4.2版本、4.2版本升级为4.4版本及4.4版本升级为5.0版本。

        :param request: Request instance for UpgradeDbInstanceVersion.
        :type request: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDbInstanceVersionRequest`
        :rtype: :class:`tencentcloud.mongodb.v20190725.models.UpgradeDbInstanceVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDbInstanceVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDbInstanceVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))