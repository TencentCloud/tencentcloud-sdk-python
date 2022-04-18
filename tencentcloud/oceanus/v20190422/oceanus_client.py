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
from tencentcloud.oceanus.v20190422 import models


class OceanusClient(AbstractClient):
    _apiVersion = '2019-04-22'
    _endpoint = 'oceanus.tencentcloudapi.com'
    _service = 'oceanus'


    def CreateJob(self, request):
        """新建作业接口，一个 AppId 最多允许创建1000个作业

        :param request: Request instance for CreateJob.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJob", params, headers=headers)
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
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateJobConfig(self, request):
        """创建作业配置，一个作业最多有100个配置版本

        :param request: Request instance for CreateJobConfig.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateJobConfigRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateJobConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJobConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateJobConfigResponse()
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


    def CreateResource(self, request):
        """创建资源接口

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResource", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateResourceResponse()
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


    def CreateResourceConfig(self, request):
        """创建资源配置接口

        :param request: Request instance for CreateResourceConfig.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceConfigRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.CreateResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateResourceConfigResponse()
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


    def DeleteResourceConfigs(self, request):
        """删除资源版本

        :param request: Request instance for DeleteResourceConfigs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourceConfigsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourceConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceConfigs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteResourceConfigsResponse()
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


    def DeleteResources(self, request):
        """删除资源接口

        :param request: Request instance for DeleteResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResources", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteResourcesResponse()
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


    def DeleteTableConfig(self, request):
        """删除作业表配置

        :param request: Request instance for DeleteTableConfig.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DeleteTableConfigRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DeleteTableConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTableConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTableConfigResponse()
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


    def DescribeJobConfigs(self, request):
        """查询作业配置列表，一次最多查询100个

        :param request: Request instance for DescribeJobConfigs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobConfigsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobConfigs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobConfigsResponse()
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


    def DescribeJobs(self, request):
        """查询作业

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobsResponse()
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


    def DescribeResourceConfigs(self, request):
        """描述资源配置接口

        :param request: Request instance for DescribeResourceConfigs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceConfigsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceConfigs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceConfigsResponse()
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


    def DescribeResourceRelatedJobs(self, request):
        """获取资源关联作业信息

        :param request: Request instance for DescribeResourceRelatedJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceRelatedJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourceRelatedJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceRelatedJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceRelatedJobsResponse()
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


    def DescribeResources(self, request):
        """描述资源接口

        :param request: Request instance for DescribeResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResources", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesResponse()
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


    def DescribeSystemResources(self, request):
        """描述系统资源接口

        :param request: Request instance for DescribeSystemResources.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.DescribeSystemResourcesRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.DescribeSystemResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSystemResources", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSystemResourcesResponse()
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


    def RunJobs(self, request):
        """批量启动或者恢复作业，批量操作数量上限20

        :param request: Request instance for RunJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.RunJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.RunJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunJobsResponse()
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


    def StopJobs(self, request):
        """批量停止作业，批量操作数量上限为20

        :param request: Request instance for StopJobs.
        :type request: :class:`tencentcloud.oceanus.v20190422.models.StopJobsRequest`
        :rtype: :class:`tencentcloud.oceanus.v20190422.models.StopJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopJobs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopJobsResponse()
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