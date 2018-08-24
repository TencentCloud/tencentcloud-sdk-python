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
from tencentcloud.tia.v20180226 import models


class TiaClient(AbstractClient):
    _apiVersion = '2018-02-26'
    _endpoint = 'tia.tencentcloudapi.com'


    def CreateJob(self, request):
        """创建训练任务

        :param request: 调用CreateJob所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateModel(self, request):
        """在指定的集群上部署一个模型，用以提供服务。

        :param request: 调用CreateModel所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.CreateModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.CreateModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateModelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteJob(self, request):
        """删除训练任务

        :param request: 调用DeleteJob所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteModel(self, request):
        """删除一个指定的Model

        :param request: 调用DeleteModel所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.DeleteModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteModelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJob(self, request):
        """获取训练任务详情

        :param request: 调用DescribeJob所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.DescribeJobRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DescribeJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeModel(self, request):
        """描述Model

        :param request: 调用DescribeModel所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.DescribeModelRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.DescribeModelResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModel", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModelResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InstallAgent(self, request):
        """安装agent

        :param request: 调用InstallAgent所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.InstallAgentRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.InstallAgentResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InstallAgent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InstallAgentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListJobs(self, request):
        """列举训练任务

        :param request: 调用ListJobs所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.ListJobsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.ListJobsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListJobs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListJobsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListModels(self, request):
        """列举某个指定集群上运行的模型。

        :param request: 调用ListModels所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.ListModelsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.ListModelsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListModels", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListModelsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryLogs(self, request):
        """查询日志

        :param request: 调用QueryLogs所需参数的结构体。
        :type request: :class:`tencentcloud.tia.v20180226.models.QueryLogsRequest`
        :rtype: :class:`tencentcloud.tia.v20180226.models.QueryLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)