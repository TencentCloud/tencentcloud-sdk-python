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
from tencentcloud.tem.v20210701 import models


class TemClient(AbstractClient):
    _apiVersion = '2021-07-01'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'


    def CreateApplication(self, request):
        """创建应用

        :param request: Request instance for CreateApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplication", params, headers=headers)
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


    def CreateApplicationAutoscaler(self, request):
        """创建弹性伸缩策略组合

        :param request: Request instance for CreateApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateApplicationAutoscalerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateConfigData(self, request):
        """创建配置

        :param request: Request instance for CreateConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConfigData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateConfigDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCosToken(self, request):
        """生成Cos临时秘钥

        :param request: Request instance for CreateCosToken.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateCosTokenRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateCosTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCosToken", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosTokenResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateEnvironment(self, request):
        """创建环境

        :param request: Request instance for CreateEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLogConfig(self, request):
        """创建日志收集配置

        :param request: Request instance for CreateLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLogConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """绑定云资源

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.tem.v20210701.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.CreateResourceResponse`

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


    def DeleteApplication(self, request):
        """服务删除
          - 停止当前运行服务
          - 删除服务相关资源
          - 删除服务

        :param request: Request instance for DeleteApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplication", params, headers=headers)
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


    def DeleteApplicationAutoscaler(self, request):
        """删除应用弹性策略组合

        :param request: Request instance for DeleteApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteApplicationAutoscalerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIngress(self, request):
        """删除 Ingress 规则

        :param request: Request instance for DeleteIngress.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeleteIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeleteIngressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIngress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIngressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeployApplication(self, request):
        """应用部署

        :param request: Request instance for DeployApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.DeployApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DeployApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployApplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationAutoscalerList(self, request):
        """获取应用弹性策略组合

        :param request: Request instance for DescribeApplicationAutoscalerList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationAutoscalerListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationAutoscalerListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationAutoscalerList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationAutoscalerListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationInfo(self, request):
        """服务基本信息查看

        :param request: Request instance for DescribeApplicationInfo.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationInfoRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeApplicationPods(self, request):
        """获取应用实例列表

        :param request: Request instance for DescribeApplicationPods.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationPodsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationPods", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationPodsResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """获取运行服务列表

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplications", params, headers=headers)
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


    def DescribeApplicationsStatus(self, request):
        """单环境下所有应用状态查看

        :param request: Request instance for DescribeApplicationsStatus.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsStatusRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeApplicationsStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplicationsStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeApplicationsStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigData(self, request):
        """查询配置详情

        :param request: Request instance for DescribeConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeConfigDataList(self, request):
        """查询配置列表

        :param request: Request instance for DescribeConfigDataList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeConfigDataListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConfigDataList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigDataListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDeployApplicationDetail(self, request):
        """获取分批发布详情

        :param request: Request instance for DescribeDeployApplicationDetail.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeDeployApplicationDetailRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeDeployApplicationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployApplicationDetail", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeployApplicationDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironment(self, request):
        """获取环境基础信息

        :param request: Request instance for DescribeEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironmentStatus(self, request):
        """获取环境状态

        :param request: Request instance for DescribeEnvironmentStatus.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentStatusRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironmentStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEnvironments(self, request):
        """获取环境列表

        :param request: Request instance for DescribeEnvironments.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentsRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeEnvironmentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEnvironments", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvironmentsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIngress(self, request):
        """查询 Ingress 规则

        :param request: Request instance for DescribeIngress.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeIngressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIngress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIngressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIngresses(self, request):
        """查询 Ingress 规则列表

        :param request: Request instance for DescribeIngresses.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeIngressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIngresses", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIngressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLogConfig(self, request):
        """查询日志收集配置详情

        :param request: Request instance for DescribeLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePagedLogConfigList(self, request):
        """查询分页的日志收集配置列表

        :param request: Request instance for DescribePagedLogConfigList.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribePagedLogConfigListRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribePagedLogConfigListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePagedLogConfigList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePagedLogConfigListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRelatedIngresses(self, request):
        """查询应用关联的 Ingress 规则列表

        :param request: Request instance for DescribeRelatedIngresses.
        :type request: :class:`tencentcloud.tem.v20210701.models.DescribeRelatedIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DescribeRelatedIngressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedIngresses", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelatedIngressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyConfigData(self, request):
        """销毁配置

        :param request: Request instance for DestroyConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyConfigData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyConfigDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyEnvironment(self, request):
        """销毁环境

        :param request: Request instance for DestroyEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyLogConfig(self, request):
        """销毁日志收集配置

        :param request: Request instance for DestroyLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.DestroyLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DestroyLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyLogConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableApplicationAutoscaler(self, request):
        """关闭应用弹性策略组合

        :param request: Request instance for DisableApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.DisableApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.DisableApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableApplicationAutoscalerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableApplicationAutoscaler(self, request):
        """启用应用弹性策略组合

        :param request: Request instance for EnableApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.EnableApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.EnableApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableApplicationAutoscalerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateApplicationPackageDownloadUrl(self, request):
        """生成应用程序包预签名下载链接

        :param request: Request instance for GenerateApplicationPackageDownloadUrl.
        :type request: :class:`tencentcloud.tem.v20210701.models.GenerateApplicationPackageDownloadUrlRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.GenerateApplicationPackageDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateApplicationPackageDownloadUrl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GenerateApplicationPackageDownloadUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationAutoscaler(self, request):
        """修改弹性伸缩策略组合

        :param request: Request instance for ModifyApplicationAutoscaler.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationAutoscalerRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationAutoscalerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationAutoscaler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationAutoscalerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationInfo(self, request):
        """修改应用基本信息

        :param request: Request instance for ModifyApplicationInfo.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationInfoRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationInfo", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationInfoResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyApplicationReplicas(self, request):
        """修改应用实例数量

        :param request: Request instance for ModifyApplicationReplicas.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationReplicasRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyApplicationReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApplicationReplicas", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyApplicationReplicasResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyConfigData(self, request):
        """编辑配置

        :param request: Request instance for ModifyConfigData.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyConfigDataRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyConfigDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConfigData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyConfigDataResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyEnvironment(self, request):
        """编辑环境

        :param request: Request instance for ModifyEnvironment.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyEnvironmentRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyEnvironmentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEnvironment", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvironmentResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIngress(self, request):
        """创建或者更新 Ingress 规则

        :param request: Request instance for ModifyIngress.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyIngressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIngress", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIngressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLogConfig(self, request):
        """编辑日志收集配置

        :param request: Request instance for ModifyLogConfig.
        :type request: :class:`tencentcloud.tem.v20210701.models.ModifyLogConfigRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ModifyLogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLogConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartApplication(self, request):
        """服务重启

        :param request: Request instance for RestartApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.RestartApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RestartApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartApplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartApplicationPod(self, request):
        """重启应用实例

        :param request: Request instance for RestartApplicationPod.
        :type request: :class:`tencentcloud.tem.v20210701.models.RestartApplicationPodRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RestartApplicationPodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartApplicationPod", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartApplicationPodResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeDeployApplication(self, request):
        """开始下一批次发布

        :param request: Request instance for ResumeDeployApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.ResumeDeployApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.ResumeDeployApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeDeployApplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResumeDeployApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RevertDeployApplication(self, request):
        """回滚分批发布

        :param request: Request instance for RevertDeployApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.RevertDeployApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RevertDeployApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevertDeployApplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RevertDeployApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RollingUpdateApplicationByVersion(self, request):
        """更新应用部署版本

        :param request: Request instance for RollingUpdateApplicationByVersion.
        :type request: :class:`tencentcloud.tem.v20210701.models.RollingUpdateApplicationByVersionRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.RollingUpdateApplicationByVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollingUpdateApplicationByVersion", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollingUpdateApplicationByVersionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopApplication(self, request):
        """服务停止

        :param request: Request instance for StopApplication.
        :type request: :class:`tencentcloud.tem.v20210701.models.StopApplicationRequest`
        :rtype: :class:`tencentcloud.tem.v20210701.models.StopApplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopApplication", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopApplicationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)