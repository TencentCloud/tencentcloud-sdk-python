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
from tencentcloud.tsf.v20180326 import models


class TsfClient(AbstractClient):
    _apiVersion = '2018-03-26'
    _endpoint = 'tsf.tencentcloudapi.com'
    _service = 'tsf'


    def AddClusterInstances(self, request):
        """添加云主机节点至TSF集群

        :param request: Request instance for AddClusterInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.AddClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AddClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddClusterInstancesResponse()
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
        """添加云主机节点至TSF集群

        :param request: Request instance for AddInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddInstances", params)
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


    def BindApiGroup(self, request):
        """网关与API分组批量绑定

        :param request: Request instance for BindApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.BindApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.BindApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindApiGroupResponse()
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


    def BindPlugin(self, request):
        """插件与网关分组/API批量绑定

        :param request: Request instance for BindPlugin.
        :type request: :class:`tencentcloud.tsf.v20180326.models.BindPluginRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.BindPluginResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindPlugin", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindPluginResponse()
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


    def ChangeApiUsableStatus(self, request):
        """启用或禁用API

        :param request: Request instance for ChangeApiUsableStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ChangeApiUsableStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ChangeApiUsableStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ChangeApiUsableStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChangeApiUsableStatusResponse()
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


    def ContinueRunFailedTaskBatch(self, request):
        """对执行失败的任务批次执行续跑

        :param request: Request instance for ContinueRunFailedTaskBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ContinueRunFailedTaskBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ContinueRunFailedTaskBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ContinueRunFailedTaskBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ContinueRunFailedTaskBatchResponse()
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


    def CreateAllGatewayApiAsync(self, request):
        """一键导入API分组

        :param request: Request instance for CreateAllGatewayApiAsync.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateAllGatewayApiAsyncRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateAllGatewayApiAsyncResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAllGatewayApiAsync", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAllGatewayApiAsyncResponse()
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


    def CreateApiGroup(self, request):
        """创建API分组

        :param request: Request instance for CreateApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApiGroupResponse()
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


    def CreateApiRateLimitRule(self, request):
        """创建API限流规则

        :param request: Request instance for CreateApiRateLimitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApiRateLimitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApiRateLimitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApiRateLimitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApiRateLimitRuleResponse()
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


    def CreateApplication(self, request):
        """创建应用

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationResponse()
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
        """创建集群

        :param request: Request instance for CreateCluster.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateClusterRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateClusterResponse`

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


    def CreateConfig(self, request):
        """创建配置项

        :param request: Request instance for CreateConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateConfigResponse()
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


    def CreateContainGroup(self, request):
        """创建容器部署组

        :param request: Request instance for CreateContainGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateContainGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateContainGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContainGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContainGroupResponse()
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


    def CreateFileConfig(self, request):
        """创建文件配置项

        :param request: Request instance for CreateFileConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateFileConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateFileConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFileConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFileConfigResponse()
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


    def CreateGatewayApi(self, request):
        """批量导入API至api分组(也支持新建API到分组)

        :param request: Request instance for CreateGatewayApi.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateGatewayApiRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateGatewayApiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGatewayApi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGatewayApiResponse()
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


    def CreateGroup(self, request):
        """创建虚拟机部署组

        :param request: Request instance for CreateGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGroupResponse()
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


    def CreateLane(self, request):
        """创建泳道

        :param request: Request instance for CreateLane.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateLaneRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateLaneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLane", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLaneResponse()
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


    def CreateLaneRule(self, request):
        """创建泳道规则

        :param request: Request instance for CreateLaneRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateLaneRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateLaneRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLaneRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLaneRuleResponse()
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


    def CreateMicroservice(self, request):
        """新增微服务

        :param request: Request instance for CreateMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMicroserviceResponse()
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


    def CreateNamespace(self, request):
        """创建命名空间

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
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


    def CreatePathRewrites(self, request):
        """创建路径重写

        :param request: Request instance for CreatePathRewrites.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreatePathRewritesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreatePathRewritesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePathRewrites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePathRewritesResponse()
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


    def CreatePublicConfig(self, request):
        """创建公共配置项

        :param request: Request instance for CreatePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreatePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreatePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePublicConfigResponse()
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


    def CreateRepository(self, request):
        """创建仓库

        :param request: Request instance for CreateRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRepositoryResponse()
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


    def CreateServerlessGroup(self, request):
        """创建Serverless部署组

        :param request: Request instance for CreateServerlessGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateServerlessGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServerlessGroupResponse()
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
        """创建任务

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateTaskResponse`

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


    def CreateTaskFlow(self, request):
        """创建工作流

        :param request: Request instance for CreateTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateTaskFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTaskFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTaskFlowResponse()
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


    def CreateUnitRule(self, request):
        """创建单元化规则

        :param request: Request instance for CreateUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.CreateUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.CreateUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUnitRuleResponse()
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


    def DeleteApiGroup(self, request):
        """删除Api分组

        :param request: Request instance for DeleteApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApiGroupResponse()
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


    def DeleteApplication(self, request):
        """删除应用

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationResponse()
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


    def DeleteConfig(self, request):
        """删除配置项

        :param request: Request instance for DeleteConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteConfigResponse()
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


    def DeleteContainerGroup(self, request):
        """删除容器部署组

        :param request: Request instance for DeleteContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContainerGroupResponse()
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


    def DeleteGroup(self, request):
        """删除容器部署组

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGroupResponse()
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


    def DeleteImageTags(self, request):
        """批量删除镜像版本

        :param request: Request instance for DeleteImageTags.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteImageTagsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteImageTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageTagsResponse()
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


    def DeleteLane(self, request):
        """删除泳道

        :param request: Request instance for DeleteLane.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteLaneRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteLaneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLane", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLaneResponse()
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


    def DeleteMicroservice(self, request):
        """删除微服务

        :param request: Request instance for DeleteMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMicroserviceResponse()
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


    def DeleteNamespace(self, request):
        """删除命名空间

        :param request: Request instance for DeleteNamespace.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteNamespaceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNamespaceResponse()
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


    def DeletePathRewrites(self, request):
        """删除路径重写

        :param request: Request instance for DeletePathRewrites.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePathRewritesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePathRewritesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePathRewrites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePathRewritesResponse()
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


    def DeletePkgs(self, request):
        """从软件仓库批量删除程序包。
        一次最多支持删除1000个包，数量超过1000，返回UpperDeleteLimit错误。

        :param request: Request instance for DeletePkgs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePkgsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePkgsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePkgs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePkgsResponse()
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


    def DeletePublicConfig(self, request):
        """删除公共配置项

        :param request: Request instance for DeletePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeletePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeletePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePublicConfigResponse()
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


    def DeleteRepository(self, request):
        """删除仓库

        :param request: Request instance for DeleteRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRepositoryResponse()
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


    def DeleteServerlessGroup(self, request):
        """删除Serverless部署组

        :param request: Request instance for DeleteServerlessGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteServerlessGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServerlessGroupResponse()
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


    def DeleteTask(self, request):
        """删除任务

        :param request: Request instance for DeleteTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTaskResponse()
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


    def DeleteUnitNamespaces(self, request):
        """删除单元化命名空间

        :param request: Request instance for DeleteUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUnitNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUnitNamespacesResponse()
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


    def DeleteUnitRule(self, request):
        """删除单元化规则

        :param request: Request instance for DeleteUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeleteUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUnitRuleResponse()
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


    def DeployContainerGroup(self, request):
        """部署容器应用

        :param request: Request instance for DeployContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployContainerGroupResponse()
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


    def DeployGroup(self, request):
        """部署虚拟机部署组应用

        :param request: Request instance for DeployGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployGroupResponse()
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


    def DeployServerlessGroup(self, request):
        """部署Serverless应用

        :param request: Request instance for DeployServerlessGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DeployServerlessGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DeployServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeployServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployServerlessGroupResponse()
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


    def DescribeApiDetail(self, request):
        """查询API详情

        :param request: Request instance for DescribeApiDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiDetailResponse()
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


    def DescribeApiGroup(self, request):
        """查询API分组

        :param request: Request instance for DescribeApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiGroupResponse()
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


    def DescribeApiGroups(self, request):
        """查询API 分组信息列表

        :param request: Request instance for DescribeApiGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiGroupsResponse()
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


    def DescribeApiRateLimitRules(self, request):
        """查询API限流规则

        :param request: Request instance for DescribeApiRateLimitRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiRateLimitRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiRateLimitRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiRateLimitRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiRateLimitRulesResponse()
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


    def DescribeApiUseDetail(self, request):
        """查询网关API监控明细数据

        :param request: Request instance for DescribeApiUseDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiUseDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiUseDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiUseDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiUseDetailResponse()
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


    def DescribeApiVersions(self, request):
        """查询API 版本

        :param request: Request instance for DescribeApiVersions.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApiVersionsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApiVersionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApiVersions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApiVersionsResponse()
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


    def DescribeApplication(self, request):
        """获取应用详情

        :param request: Request instance for DescribeApplication.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationResponse()
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


    def DescribeApplicationAttribute(self, request):
        """获取应用列表其它字段，如实例数量信息等

        :param request: Request instance for DescribeApplicationAttribute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationAttributeRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplicationAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationAttributeResponse()
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


    def DescribeApplications(self, request):
        """获取应用列表

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationsResponse()
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


    def DescribeBasicResourceUsage(self, request):
        """TSF基本资源信息概览接口

        :param request: Request instance for DescribeBasicResourceUsage.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeBasicResourceUsageRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeBasicResourceUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBasicResourceUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicResourceUsageResponse()
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


    def DescribeClusterInstances(self, request):
        """查询集群实例

        :param request: Request instance for DescribeClusterInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeClusterInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeClusterInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClusterInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterInstancesResponse()
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


    def DescribeConfig(self, request):
        """查询配置

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeConfigReleaseLogs(self, request):
        """查询配置发布历史

        :param request: Request instance for DescribeConfigReleaseLogs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleaseLogsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleaseLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigReleaseLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigReleaseLogsResponse()
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


    def DescribeConfigReleases(self, request):
        """查询配置发布信息

        :param request: Request instance for DescribeConfigReleases.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleasesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigReleases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigReleasesResponse()
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


    def DescribeConfigSummary(self, request):
        """查询配置汇总列表

        :param request: Request instance for DescribeConfigSummary.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigSummaryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigSummaryResponse()
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


    def DescribeConfigs(self, request):
        """查询配置项列表

        :param request: Request instance for DescribeConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigsResponse()
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


    def DescribeContainerEvents(self, request):
        """获取容器事件列表

        :param request: Request instance for DescribeContainerEvents.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerEventsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerEventsResponse()
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


    def DescribeContainerGroupDetail(self, request):
        """容器部署组详情

        :param request: Request instance for DescribeContainerGroupDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerGroupDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerGroupDetailResponse()
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


    def DescribeContainerGroups(self, request):
        """容器部署组列表

        :param request: Request instance for DescribeContainerGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeContainerGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContainerGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContainerGroupsResponse()
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


    def DescribeCreateGatewayApiStatus(self, request):
        """查询一键导入API分组任务的状态

        :param request: Request instance for DescribeCreateGatewayApiStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeCreateGatewayApiStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeCreateGatewayApiStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCreateGatewayApiStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCreateGatewayApiStatusResponse()
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


    def DescribeDownloadInfo(self, request):
        """TSF上传的程序包存放在腾讯云对象存储（COS）中，通过该API可以获取从COS下载程序包需要的信息，包括包所在的桶、存储路径、鉴权信息等，之后使用COS API（或SDK）进行下载。
        COS相关文档请查阅：https://cloud.tencent.com/document/product/436

        :param request: Request instance for DescribeDownloadInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeDownloadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeDownloadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDownloadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDownloadInfoResponse()
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


    def DescribeEnabledUnitRule(self, request):
        """查询生效的单元化规则

        :param request: Request instance for DescribeEnabledUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeEnabledUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeEnabledUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnabledUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnabledUnitRuleResponse()
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


    def DescribeFileConfigs(self, request):
        """查询文件配置项列表

        :param request: Request instance for DescribeFileConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeFileConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeFileConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileConfigsResponse()
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


    def DescribeFlowLastBatchState(self, request):
        """查询工作流最新一个批次的状态信息

        :param request: Request instance for DescribeFlowLastBatchState.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeFlowLastBatchStateRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeFlowLastBatchStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowLastBatchState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowLastBatchStateResponse()
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


    def DescribeGatewayAllGroupApis(self, request):
        """查询网关所有分组下Api列表

        :param request: Request instance for DescribeGatewayAllGroupApis.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayAllGroupApisRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayAllGroupApisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGatewayAllGroupApis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayAllGroupApisResponse()
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


    def DescribeGatewayMonitorOverview(self, request):
        """查询网关监控概览

        :param request: Request instance for DescribeGatewayMonitorOverview.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayMonitorOverviewRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGatewayMonitorOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGatewayMonitorOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayMonitorOverviewResponse()
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


    def DescribeGroup(self, request):
        """查询虚拟机部署组详情

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupResponse()
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


    def DescribeGroupBindedGateways(self, request):
        """查询某个API分组已绑定的网关部署组信息列表

        :param request: Request instance for DescribeGroupBindedGateways.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupBindedGatewaysRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupBindedGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupBindedGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupBindedGatewaysResponse()
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


    def DescribeGroupGateways(self, request):
        """查询某个网关绑定的API 分组信息列表

        :param request: Request instance for DescribeGroupGateways.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupGatewaysRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupGatewaysResponse()
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


    def DescribeGroupInstances(self, request):
        """查询虚拟机部署组云主机列表

        :param request: Request instance for DescribeGroupInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupInstancesResponse()
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


    def DescribeGroupUseDetail(self, request):
        """查询网关分组监控明细数据

        :param request: Request instance for DescribeGroupUseDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupUseDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupUseDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupUseDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupUseDetailResponse()
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


    def DescribeGroups(self, request):
        """获取虚拟机部署组列表

        :param request: Request instance for DescribeGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupsResponse()
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


    def DescribeGroupsWithPlugin(self, request):
        """查询某个插件下绑定或未绑定的API分组

        :param request: Request instance for DescribeGroupsWithPlugin.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsWithPluginRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeGroupsWithPluginResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupsWithPlugin", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupsWithPluginResponse()
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


    def DescribeImageRepository(self, request):
        """镜像仓库列表

        :param request: Request instance for DescribeImageRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeImageRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeImageRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageRepositoryResponse()
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


    def DescribeImageTags(self, request):
        """镜像版本列表

        :param request: Request instance for DescribeImageTags.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeImageTagsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeImageTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageTagsResponse()
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


    def DescribeLaneRules(self, request):
        """查询泳道规则列表

        :param request: Request instance for DescribeLaneRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeLaneRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeLaneRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLaneRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLaneRulesResponse()
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


    def DescribeLanes(self, request):
        """查询泳道列表

        :param request: Request instance for DescribeLanes.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeLanesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeLanesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLanes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLanesResponse()
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


    def DescribeMicroservice(self, request):
        """查询微服务详情

        :param request: Request instance for DescribeMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMicroserviceResponse()
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


    def DescribeMicroservices(self, request):
        """获取微服务列表

        :param request: Request instance for DescribeMicroservices.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroservicesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMicroservicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMicroservices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMicroservicesResponse()
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


    def DescribeMsApiList(self, request):
        """查询服务API列表

        :param request: Request instance for DescribeMsApiList.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeMsApiListRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeMsApiListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMsApiList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMsApiListResponse()
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


    def DescribePathRewrite(self, request):
        """查询路径重写

        :param request: Request instance for DescribePathRewrite.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewriteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePathRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePathRewriteResponse()
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


    def DescribePathRewrites(self, request):
        """查询路径重写列表

        :param request: Request instance for DescribePathRewrites.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewritesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePathRewritesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePathRewrites", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePathRewritesResponse()
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


    def DescribePkgs(self, request):
        """无

        :param request: Request instance for DescribePkgs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePkgsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePkgsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePkgs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePkgsResponse()
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


    def DescribePluginInstances(self, request):
        """分页查询网关分组/API绑定（或未绑定）的插件列表

        :param request: Request instance for DescribePluginInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePluginInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePluginInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePluginInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePluginInstancesResponse()
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


    def DescribePodInstances(self, request):
        """获取部署组实例列表

        :param request: Request instance for DescribePodInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePodInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePodInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePodInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePodInstancesResponse()
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


    def DescribePublicConfig(self, request):
        """查询公共配置（单条）

        :param request: Request instance for DescribePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigResponse()
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


    def DescribePublicConfigReleaseLogs(self, request):
        """查询公共配置发布历史

        :param request: Request instance for DescribePublicConfigReleaseLogs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleaseLogsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleaseLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigReleaseLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigReleaseLogsResponse()
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


    def DescribePublicConfigReleases(self, request):
        """查询公共配置发布信息

        :param request: Request instance for DescribePublicConfigReleases.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleasesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigReleasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigReleases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigReleasesResponse()
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


    def DescribePublicConfigSummary(self, request):
        """查询公共配置汇总列表

        :param request: Request instance for DescribePublicConfigSummary.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigSummaryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigSummaryResponse()
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


    def DescribePublicConfigs(self, request):
        """查询公共配置项列表

        :param request: Request instance for DescribePublicConfigs.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribePublicConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublicConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublicConfigsResponse()
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


    def DescribeReleasedConfig(self, request):
        """查询group发布的配置

        :param request: Request instance for DescribeReleasedConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeReleasedConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeReleasedConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReleasedConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReleasedConfigResponse()
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


    def DescribeRepositories(self, request):
        """查询仓库列表

        :param request: Request instance for DescribeRepositories.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoriesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoriesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepositories", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepositoriesResponse()
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


    def DescribeRepository(self, request):
        """查询仓库信息

        :param request: Request instance for DescribeRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepositoryResponse()
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


    def DescribeServerlessGroup(self, request):
        """查询Serverless部署组明细

        :param request: Request instance for DescribeServerlessGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeServerlessGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeServerlessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServerlessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServerlessGroupResponse()
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


    def DescribeServerlessGroups(self, request):
        """查询Serverless部署组列表

        :param request: Request instance for DescribeServerlessGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeServerlessGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeServerlessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServerlessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServerlessGroupsResponse()
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


    def DescribeSimpleApplications(self, request):
        """查询简单应用列表

        :param request: Request instance for DescribeSimpleApplications.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleApplicationsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleApplicationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleApplications", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleApplicationsResponse()
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


    def DescribeSimpleClusters(self, request):
        """查询简单集群列表

        :param request: Request instance for DescribeSimpleClusters.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleClustersRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleClustersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleClusters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleClustersResponse()
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


    def DescribeSimpleGroups(self, request):
        """查询简单部署组列表

        :param request: Request instance for DescribeSimpleGroups.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleGroupsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleGroupsResponse()
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


    def DescribeSimpleNamespaces(self, request):
        """查询简单命名空间列表

        :param request: Request instance for DescribeSimpleNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeSimpleNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSimpleNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSimpleNamespacesResponse()
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
        """查询任务详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
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


    def DescribeTaskLastStatus(self, request):
        """查询任务最近一次执行状态

        :param request: Request instance for DescribeTaskLastStatus.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskLastStatusRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskLastStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskLastStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskLastStatusResponse()
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


    def DescribeTaskRecords(self, request):
        """翻页查询任务列表

        :param request: Request instance for DescribeTaskRecords.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskRecordsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeTaskRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskRecordsResponse()
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


    def DescribeUnitApiUseDetail(self, request):
        """查询网关API监控明细数据（仅单元化网关），非单元化网关使用DescribeApiUseDetail

        :param request: Request instance for DescribeUnitApiUseDetail.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitApiUseDetailRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitApiUseDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnitApiUseDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnitApiUseDetailResponse()
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


    def DescribeUnitNamespaces(self, request):
        """查询单元化命名空间列表

        :param request: Request instance for DescribeUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnitNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnitNamespacesResponse()
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


    def DescribeUnitRule(self, request):
        """查询单元化规则详情

        :param request: Request instance for DescribeUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnitRuleResponse()
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


    def DescribeUnitRules(self, request):
        """查询单元化规则列表

        :param request: Request instance for DescribeUnitRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUnitRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUnitRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUnitRulesResponse()
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


    def DescribeUploadInfo(self, request):
        """TSF会将软件包上传到腾讯云对象存储（COS）。调用此接口获取上传信息，如目标地域，桶，包Id，存储路径，鉴权信息等，之后请使用COS API（或SDK）进行上传。
        COS相关文档请查阅：https://cloud.tencent.com/document/product/436

        :param request: Request instance for DescribeUploadInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUploadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUploadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUploadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUploadInfoResponse()
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


    def DescribeUsableUnitNamespaces(self, request):
        """查询可用于被导入的命名空间列表

        :param request: Request instance for DescribeUsableUnitNamespaces.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DescribeUsableUnitNamespacesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DescribeUsableUnitNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsableUnitNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsableUnitNamespacesResponse()
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


    def DisableTask(self, request):
        """停用任务

        :param request: Request instance for DisableTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableTaskResponse()
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


    def DisableTaskFlow(self, request):
        """停用工作流

        :param request: Request instance for DisableTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableTaskFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableTaskFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableTaskFlowResponse()
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


    def DisableUnitRoute(self, request):
        """禁用单元化路由

        :param request: Request instance for DisableUnitRoute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRouteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableUnitRoute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableUnitRouteResponse()
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


    def DisableUnitRule(self, request):
        """禁用单元化规则

        :param request: Request instance for DisableUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DisableUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableUnitRuleResponse()
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


    def DraftApiGroup(self, request):
        """下线Api分组

        :param request: Request instance for DraftApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.DraftApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.DraftApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DraftApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DraftApiGroupResponse()
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


    def EnableTask(self, request):
        """启用任务

        :param request: Request instance for EnableTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableTaskResponse()
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


    def EnableTaskFlow(self, request):
        """启用工作流

        :param request: Request instance for EnableTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableTaskFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableTaskFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableTaskFlowResponse()
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


    def EnableUnitRoute(self, request):
        """启用单元化路由

        :param request: Request instance for EnableUnitRoute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRouteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableUnitRoute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableUnitRouteResponse()
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


    def EnableUnitRule(self, request):
        """启用单元化规则

        :param request: Request instance for EnableUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.EnableUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableUnitRuleResponse()
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


    def ExecuteTask(self, request):
        """手动执行一次任务。

        :param request: Request instance for ExecuteTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExecuteTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteTaskResponse()
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


    def ExecuteTaskFlow(self, request):
        """执行一次工作流

        :param request: Request instance for ExecuteTaskFlow.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskFlowRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExecuteTaskFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExecuteTaskFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteTaskFlowResponse()
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


    def ExpandGroup(self, request):
        """虚拟机部署组添加实例

        :param request: Request instance for ExpandGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ExpandGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ExpandGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExpandGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExpandGroupResponse()
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


    def ModifyContainerGroup(self, request):
        """修改容器部署组

        :param request: Request instance for ModifyContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerGroupResponse()
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


    def ModifyContainerReplicas(self, request):
        """修改容器部署组实例数

        :param request: Request instance for ModifyContainerReplicas.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerReplicasRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyContainerReplicasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContainerReplicas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContainerReplicasResponse()
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


    def ModifyLane(self, request):
        """更新泳道信息

        :param request: Request instance for ModifyLane.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLane", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLaneResponse()
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


    def ModifyLaneRule(self, request):
        """更新泳道规则

        :param request: Request instance for ModifyLaneRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyLaneRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLaneRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLaneRuleResponse()
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


    def ModifyMicroservice(self, request):
        """修改微服务详情

        :param request: Request instance for ModifyMicroservice.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyMicroserviceRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyMicroserviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMicroservice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMicroserviceResponse()
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


    def ModifyPathRewrite(self, request):
        """修改路径重写

        :param request: Request instance for ModifyPathRewrite.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyPathRewriteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyPathRewriteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPathRewrite", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPathRewriteResponse()
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


    def ModifyTask(self, request):
        """修改任务

        :param request: Request instance for ModifyTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTaskResponse()
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


    def ModifyUploadInfo(self, request):
        """调用该接口和COS的上传接口后，需要调用此接口更新TSF中保存的程序包状态。
        调用此接口完成后，才标志上传包流程结束。

        :param request: Request instance for ModifyUploadInfo.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ModifyUploadInfoRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ModifyUploadInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUploadInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUploadInfoResponse()
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


    def RedoTask(self, request):
        """重新执行任务

        :param request: Request instance for RedoTask.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RedoTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RedoTaskResponse()
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


    def RedoTaskBatch(self, request):
        """重新执行任务批次

        :param request: Request instance for RedoTaskBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RedoTaskBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RedoTaskBatchResponse()
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


    def RedoTaskExecute(self, request):
        """重新执行在某个节点上执行任务。

        :param request: Request instance for RedoTaskExecute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskExecuteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskExecuteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RedoTaskExecute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RedoTaskExecuteResponse()
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


    def RedoTaskFlowBatch(self, request):
        """重新执行工作流批次

        :param request: Request instance for RedoTaskFlowBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RedoTaskFlowBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RedoTaskFlowBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RedoTaskFlowBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RedoTaskFlowBatchResponse()
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


    def ReleaseApiGroup(self, request):
        """发布Api分组

        :param request: Request instance for ReleaseApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseApiGroupResponse()
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


    def ReleaseConfig(self, request):
        """发布配置

        :param request: Request instance for ReleaseConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseConfigResponse()
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


    def ReleaseFileConfig(self, request):
        """发布文件配置

        :param request: Request instance for ReleaseFileConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleaseFileConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleaseFileConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseFileConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseFileConfigResponse()
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


    def ReleasePublicConfig(self, request):
        """发布公共配置

        :param request: Request instance for ReleasePublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ReleasePublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ReleasePublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleasePublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleasePublicConfigResponse()
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


    def RemoveInstances(self, request):
        """从 TSF 集群中批量移除云主机节点

        :param request: Request instance for RemoveInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RemoveInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RemoveInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveInstancesResponse()
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


    def RevocationConfig(self, request):
        """撤回已发布的配置

        :param request: Request instance for RevocationConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RevocationConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RevocationConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevocationConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevocationConfigResponse()
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


    def RevocationPublicConfig(self, request):
        """撤回已发布的公共配置

        :param request: Request instance for RevocationPublicConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RevocationPublicConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RevocationPublicConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RevocationPublicConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevocationPublicConfigResponse()
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


    def RollbackConfig(self, request):
        """回滚配置

        :param request: Request instance for RollbackConfig.
        :type request: :class:`tencentcloud.tsf.v20180326.models.RollbackConfigRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.RollbackConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackConfigResponse()
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


    def SearchBusinessLog(self, request):
        """业务日志搜索

        :param request: Request instance for SearchBusinessLog.
        :type request: :class:`tencentcloud.tsf.v20180326.models.SearchBusinessLogRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.SearchBusinessLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchBusinessLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchBusinessLogResponse()
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


    def SearchStdoutLog(self, request):
        """标准输出日志搜索

        :param request: Request instance for SearchStdoutLog.
        :type request: :class:`tencentcloud.tsf.v20180326.models.SearchStdoutLogRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.SearchStdoutLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchStdoutLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchStdoutLogResponse()
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


    def ShrinkGroup(self, request):
        """下线部署组所有机器实例

        :param request: Request instance for ShrinkGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ShrinkGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ShrinkGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShrinkGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShrinkGroupResponse()
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


    def ShrinkInstances(self, request):
        """虚拟机部署组下线实例

        :param request: Request instance for ShrinkInstances.
        :type request: :class:`tencentcloud.tsf.v20180326.models.ShrinkInstancesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.ShrinkInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ShrinkInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ShrinkInstancesResponse()
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


    def StartContainerGroup(self, request):
        """启动容器部署组

        :param request: Request instance for StartContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StartContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StartContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartContainerGroupResponse()
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


    def StartGroup(self, request):
        """启动分组

        :param request: Request instance for StartGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StartGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StartGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartGroupResponse()
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


    def StopContainerGroup(self, request):
        """停止容器部署组

        :param request: Request instance for StopContainerGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopContainerGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopContainerGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopContainerGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopContainerGroupResponse()
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


    def StopGroup(self, request):
        """停止虚拟机部署组

        :param request: Request instance for StopGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopGroupResponse()
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


    def StopTaskBatch(self, request):
        """停止执行中的任务批次， 非运行中的任务不可调用。

        :param request: Request instance for StopTaskBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopTaskBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopTaskBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopTaskBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopTaskBatchResponse()
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


    def StopTaskExecute(self, request):
        """停止正在某个节点上执行的任务

        :param request: Request instance for StopTaskExecute.
        :type request: :class:`tencentcloud.tsf.v20180326.models.StopTaskExecuteRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.StopTaskExecuteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopTaskExecute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopTaskExecuteResponse()
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


    def TerminateTaskFlowBatch(self, request):
        """停止一个工作流批次

        :param request: Request instance for TerminateTaskFlowBatch.
        :type request: :class:`tencentcloud.tsf.v20180326.models.TerminateTaskFlowBatchRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.TerminateTaskFlowBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateTaskFlowBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTaskFlowBatchResponse()
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


    def UnbindApiGroup(self, request):
        """API分组批量与网关解绑

        :param request: Request instance for UnbindApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UnbindApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UnbindApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindApiGroupResponse()
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


    def UpdateApiGroup(self, request):
        """更新Api分组

        :param request: Request instance for UpdateApiGroup.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiGroupRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateApiGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateApiGroupResponse()
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


    def UpdateApiRateLimitRule(self, request):
        """更新API限流规则

        :param request: Request instance for UpdateApiRateLimitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateApiRateLimitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateApiRateLimitRuleResponse()
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


    def UpdateApiRateLimitRules(self, request):
        """批量更新API限流规则

        :param request: Request instance for UpdateApiRateLimitRules.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRulesRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiRateLimitRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateApiRateLimitRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateApiRateLimitRulesResponse()
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


    def UpdateApiTimeouts(self, request):
        """批量更新API超时

        :param request: Request instance for UpdateApiTimeouts.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateApiTimeoutsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateApiTimeoutsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateApiTimeouts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateApiTimeoutsResponse()
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


    def UpdateGatewayApi(self, request):
        """更新API

        :param request: Request instance for UpdateGatewayApi.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateGatewayApiRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateGatewayApiResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateGatewayApi", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGatewayApiResponse()
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


    def UpdateHealthCheckSettings(self, request):
        """更新健康检查配置

        :param request: Request instance for UpdateHealthCheckSettings.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateHealthCheckSettingsRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateHealthCheckSettingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateHealthCheckSettings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateHealthCheckSettingsResponse()
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


    def UpdateRepository(self, request):
        """更新仓库信息

        :param request: Request instance for UpdateRepository.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateRepositoryRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateRepositoryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRepository", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRepositoryResponse()
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


    def UpdateUnitRule(self, request):
        """更新单元化规则

        :param request: Request instance for UpdateUnitRule.
        :type request: :class:`tencentcloud.tsf.v20180326.models.UpdateUnitRuleRequest`
        :rtype: :class:`tencentcloud.tsf.v20180326.models.UpdateUnitRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateUnitRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateUnitRuleResponse()
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