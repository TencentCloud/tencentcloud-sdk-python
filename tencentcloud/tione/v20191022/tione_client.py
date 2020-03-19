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
from tencentcloud.tione.v20191022 import models


class TioneClient(AbstractClient):
    _apiVersion = '2019-10-22'
    _endpoint = 'tione.tencentcloudapi.com'


    def CreateNotebookInstance(self, request):
        """创建Notebook实例

        :param request: Request instance for CreateNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreateNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreateNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNotebookInstanceResponse()
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


    def CreatePresignedNotebookInstanceUrl(self, request):
        """创建Notebook授权Url

        :param request: Request instance for CreatePresignedNotebookInstanceUrl.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreatePresignedNotebookInstanceUrlRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreatePresignedNotebookInstanceUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePresignedNotebookInstanceUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePresignedNotebookInstanceUrlResponse()
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


    def CreateTrainingJob(self, request):
        """创建训练任务

        :param request: Request instance for CreateTrainingJob.
        :type request: :class:`tencentcloud.tione.v20191022.models.CreateTrainingJobRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.CreateTrainingJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrainingJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTrainingJobResponse()
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


    def DeleteNotebookInstance(self, request):
        """删除notebook实例

        :param request: Request instance for DeleteNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.DeleteNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DeleteNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNotebookInstanceResponse()
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


    def DescribeNotebookInstance(self, request):
        """查询Notebook实例详情

        :param request: Request instance for DescribeNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotebookInstanceResponse()
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


    def DescribeNotebookInstances(self, request):
        """查询Notebook实例列表

        :param request: Request instance for DescribeNotebookInstances.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstancesRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeNotebookInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNotebookInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNotebookInstancesResponse()
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


    def DescribeTrainingJob(self, request):
        """查询训练任务

        :param request: Request instance for DescribeTrainingJob.
        :type request: :class:`tencentcloud.tione.v20191022.models.DescribeTrainingJobRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.DescribeTrainingJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrainingJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrainingJobResponse()
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


    def StartNotebookInstance(self, request):
        """启动Notebook实例

        :param request: Request instance for StartNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.StartNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.StartNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartNotebookInstanceResponse()
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


    def StopNotebookInstance(self, request):
        """停止Notebook实例

        :param request: Request instance for StopNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.StopNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.StopNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopNotebookInstanceResponse()
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


    def StopTrainingJob(self, request):
        """停止训练任务

        :param request: Request instance for StopTrainingJob.
        :type request: :class:`tencentcloud.tione.v20191022.models.StopTrainingJobRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.StopTrainingJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopTrainingJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopTrainingJobResponse()
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


    def UpdateNotebookInstance(self, request):
        """更新Notebook实例

        :param request: Request instance for UpdateNotebookInstance.
        :type request: :class:`tencentcloud.tione.v20191022.models.UpdateNotebookInstanceRequest`
        :rtype: :class:`tencentcloud.tione.v20191022.models.UpdateNotebookInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateNotebookInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateNotebookInstanceResponse()
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