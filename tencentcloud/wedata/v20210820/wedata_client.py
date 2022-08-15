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
from tencentcloud.wedata.v20210820 import models


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'


    def BatchDeleteTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量删除任务，仅对任务状态为”已停止“有效；

        :param request: Request instance for BatchDeleteTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteTasksNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchDeleteTasksNewResponse()
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


    def BatchModifyOwnersNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量修改任务责任人

        :param request: Request instance for BatchModifyOwnersNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOwnersNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOwnersNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyOwnersNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchModifyOwnersNewResponse()
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


    def BatchStopTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        仅对任务状态为”调度中“和”已暂停“有效，对所选任务的任务实例进行终止，并停止调度

        :param request: Request instance for BatchStopTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopTasksNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BatchStopTasksNewResponse()
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


    def CreateFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建文件夹

        :param request: Request instance for CreateFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFolder", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFolderResponse()
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
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建任务

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
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


    def CreateWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建工作流

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflow", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWorkflowResponse()
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


    def DeleteFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除文件夹

        :param request: Request instance for DeleteFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFolder", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFolderResponse()
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


    def DeleteWorkflowNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除工作流

        :param request: Request instance for DeleteWorkflowNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWorkflowNewResponse()
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


    def DescribeDependTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        根据层级查找上/下游任务节点

        :param request: Request instance for DescribeDependTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependTasksNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDependTasksNewResponse()
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


    def DescribeFolderList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        拉取文件夹目录

        :param request: Request instance for DescribeFolderList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFolderListResponse()
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


    def DescribeFolderWorkflowList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        拉取文件夹下的工作流

        :param request: Request instance for DescribeFolderWorkflowList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderWorkflowList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFolderWorkflowListResponse()
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


    def DescribeInstanceLogs(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        获取实例日志列表

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceLogsResponse()
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


    def DescribeProject(self, request):
        """获取项目信息

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectResponse()
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


    def DescribeRelatedInstances(self, request):
        """查询任务实例的关联实例列表

        :param request: Request instance for DescribeRelatedInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelatedInstancesResponse()
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


    def DescribeTaskDetail(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        查询任务具体详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTaskInstances(self, request):
        """查询任务实例列表

        :param request: Request instance for DescribeTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInstancesResponse()
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


    def DescribeTaskScript(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        查询任务脚本

        :param request: Request instance for DescribeTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskScript", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskScriptResponse()
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


    def DescribeTasksByPage(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        根据工作流分页查询任务

        :param request: Request instance for DescribeTasksByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksByPage", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksByPageResponse()
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


    def ForceSucInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量置成功

        :param request: Request instance for ForceSucInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ForceSucInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ForceSucInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForceSucInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ForceSucInstancesResponse()
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


    def FreezeTasks(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量冻结任务

        :param request: Request instance for FreezeTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FreezeTasksResponse()
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


    def FreezeTasksByMultiWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        基于多个工作流进行批量冻结任务操作

        :param request: Request instance for FreezeTasksByMultiWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByMultiWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByMultiWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasksByMultiWorkflow", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.FreezeTasksByMultiWorkflowResponse()
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


    def KillInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量终止操作

        :param request: Request instance for KillInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.KillInstancesResponse()
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


    def MakeUpTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        任务批量补录，调度状态任务才可以补录；



        :param request: Request instance for MakeUpTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpTasksNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MakeUpTasksNewResponse()
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


    def MakeUpWorkflowNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        工作流下所有任务的补录

        :param request: Request instance for MakeUpWorkflowNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpWorkflowNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpWorkflowNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpWorkflowNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MakeUpWorkflowNewResponse()
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


    def ModifyFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        文件夹更新

        :param request: Request instance for ModifyFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFolder", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFolderResponse()
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


    def ModifyTaskInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新任务

        :param request: Request instance for ModifyTaskInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskInfoResponse()
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


    def ModifyTaskLinks(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        添加父任务依赖

        :param request: Request instance for ModifyTaskLinks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskLinks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskLinksResponse()
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


    def ModifyTaskScript(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        修改任务脚本

        :param request: Request instance for ModifyTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskScript", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskScriptResponse()
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


    def ModifyWorkflowInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新工作流

        :param request: Request instance for ModifyWorkflowInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWorkflowInfoResponse()
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


    def ModifyWorkflowSchedule(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新工作流调度

        :param request: Request instance for ModifyWorkflowSchedule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowSchedule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWorkflowScheduleResponse()
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


    def RegisterEvent(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        注册事件

        :param request: Request instance for RegisterEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterEventResponse()
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


    def RegisterEventListener(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        注册事件监听器

        :param request: Request instance for RegisterEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEventListener", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterEventListenerResponse()
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


    def RerunInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量重跑

        :param request: Request instance for RerunInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RerunInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RerunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunInstances", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RerunInstancesResponse()
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


    def RunTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        运行任务

        :param request: Request instance for RunTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunTaskResponse()
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


    def SetTaskAlarmNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        设置任务告警，新建/更新告警信息（最新）

        :param request: Request instance for SetTaskAlarmNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTaskAlarmNew", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTaskAlarmNewResponse()
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


    def SubmitTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        提交任务

        :param request: Request instance for SubmitTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitTaskResponse()
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


    def SubmitWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        提交工作流

        :param request: Request instance for SubmitWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitWorkflow", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SubmitWorkflowResponse()
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


    def TriggerEvent(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        触发事件

        :param request: Request instance for TriggerEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerEvent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TriggerEventResponse()
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