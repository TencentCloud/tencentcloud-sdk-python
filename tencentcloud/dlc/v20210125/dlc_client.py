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
from tencentcloud.dlc.v20210125 import models


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.tencentcloudapi.com'
    _service = 'dlc'


    def AddUsersToWorkGroup(self, request):
        """添加用户到工作组

        :param request: Request instance for AddUsersToWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AddUsersToWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AddUsersToWorkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddUsersToWorkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUsersToWorkGroupResponse()
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


    def AttachUserPolicy(self, request):
        """绑定鉴权策略到用户

        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachUserPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachUserPolicyResponse()
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


    def AttachWorkGroupPolicy(self, request):
        """绑定鉴权策略到工作组

        :param request: Request instance for AttachWorkGroupPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachWorkGroupPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachWorkGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachWorkGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachWorkGroupPolicyResponse()
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


    def BindWorkGroupsToUser(self, request):
        """绑定工作组到用户

        :param request: Request instance for BindWorkGroupsToUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.BindWorkGroupsToUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.BindWorkGroupsToUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindWorkGroupsToUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindWorkGroupsToUserResponse()
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


    def CancelTask(self, request):
        """本接口（CancelTask），用于取消任务执行

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CancelTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CancelTaskResponse()
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


    def CreateDatabase(self, request):
        """本接口（CreateDatabase）用于生成建库SQL语句。

        :param request: Request instance for CreateDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDatabaseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDatabase", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDatabaseResponse()
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


    def CreateScript(self, request):
        """该接口（CreateScript）用于创建sql脚本。

        :param request: Request instance for CreateScript.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateScriptRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateScriptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateScript", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateScriptResponse()
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


    def CreateStoreLocation(self, request):
        """该接口（CreateStoreLocation）新增或覆盖计算结果存储位置。

        :param request: Request instance for CreateStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateStoreLocationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateStoreLocation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateStoreLocationResponse()
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


    def CreateTable(self, request):
        """本接口（CreateTable）用于生成建表SQL。

        :param request: Request instance for CreateTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTableResponse()
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


    def CreateTask(self, request):
        """本接口（CreateTask）用于创建sql查询任务。（推荐使用CreateTasks接口）

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskResponse()
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


    def CreateTasks(self, request):
        """本接口（CreateTasks），用于批量创建任务

        :param request: Request instance for CreateTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTasksResponse()
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


    def CreateTasksInOrder(self, request):
        """按顺序创建任务（已经废弃，后期不再维护，请使用接口CreateTasks）

        :param request: Request instance for CreateTasksInOrder.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTasksInOrderRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTasksInOrderResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTasksInOrder", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTasksInOrderResponse()
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


    def CreateUser(self, request):
        """创建用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserResponse()
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


    def CreateWorkGroup(self, request):
        """创建工作组

        :param request: Request instance for CreateWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateWorkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWorkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWorkGroupResponse()
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


    def DeleteScript(self, request):
        """该接口（DeleteScript）用于删除sql脚本。

        :param request: Request instance for DeleteScript.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteScriptRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteScriptResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScript", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScriptResponse()
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


    def DeleteUser(self, request):
        """删除用户

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUserResponse()
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


    def DeleteUsersFromWorkGroup(self, request):
        """从工作组中删除用户

        :param request: Request instance for DeleteUsersFromWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUsersFromWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUsersFromWorkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUsersFromWorkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUsersFromWorkGroupResponse()
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


    def DeleteWorkGroup(self, request):
        """删除工作组

        :param request: Request instance for DeleteWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteWorkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWorkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWorkGroupResponse()
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


    def DescribeDatabases(self, request):
        """本接口（DescribeDatabases）用于查询数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
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


    def DescribeScripts(self, request):
        """该接口（DescribeScripts）用于获取所有SQL查询。

        :param request: Request instance for DescribeScripts.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeScriptsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeScriptsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScripts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScriptsResponse()
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


    def DescribeStoreLocation(self, request):
        """查询计算结果存储位置。

        :param request: Request instance for DescribeStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeStoreLocationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStoreLocation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStoreLocationResponse()
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


    def DescribeTable(self, request):
        """本接口（DescribeTable），用于查询单个表的详细信息。

        :param request: Request instance for DescribeTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTableResponse()
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
        """本接口（DescribeTables）用于查询数据表列表。

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesResponse`

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


    def DescribeTasks(self, request):
        """该接口（DescribleTasks）用于查询任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksResponse`

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


    def DescribeUsers(self, request):
        """获取用户列表信息

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsersResponse()
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


    def DescribeViews(self, request):
        """本接口（DescribeViews）用于查询数据视图列表。

        :param request: Request instance for DescribeViews.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeViewsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeViewsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeViews", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeViewsResponse()
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


    def DescribeWorkGroups(self, request):
        """获取工作组列表

        :param request: Request instance for DescribeWorkGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWorkGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWorkGroupsResponse()
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


    def DetachUserPolicy(self, request):
        """解绑用户鉴权策略

        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DetachUserPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachUserPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachUserPolicyResponse()
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


    def DetachWorkGroupPolicy(self, request):
        """解绑工作组鉴权策略

        :param request: Request instance for DetachWorkGroupPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DetachWorkGroupPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DetachWorkGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachWorkGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachWorkGroupPolicyResponse()
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


    def ModifyUser(self, request):
        """修改用户信息

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserResponse()
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


    def ModifyWorkGroup(self, request):
        """修改工作组信息

        :param request: Request instance for ModifyWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyWorkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWorkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWorkGroupResponse()
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


    def UnbindWorkGroupsFromUser(self, request):
        """解绑用户上的用户组

        :param request: Request instance for UnbindWorkGroupsFromUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UnbindWorkGroupsFromUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UnbindWorkGroupsFromUserResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindWorkGroupsFromUser", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindWorkGroupsFromUserResponse()
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