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
from tencentcloud.tiems.v20190416 import models


class TiemsClient(AbstractClient):
    _apiVersion = '2019-04-16'
    _endpoint = 'tiems.tencentcloudapi.com'
    _service = 'tiems'


    def CreateJob(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        创建任务

        :param request: Request instance for CreateJob.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateJobRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRsgAsGroup(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        创建资源组的伸缩组。当前一个资源组仅允许创建一个伸缩组。

        :param request: Request instance for CreateRsgAsGroup.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateRsgAsGroupRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateRsgAsGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRsgAsGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRsgAsGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRuntime(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        创建运行环境

        :param request: Request instance for CreateRuntime.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateRuntimeRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateRuntimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRuntime", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuntimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateService(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        创建服务

        :param request: Request instance for CreateService.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServiceConfig(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        创建服务配置

        :param request: Request instance for CreateServiceConfig.
        :type request: :class:`tencentcloud.tiems.v20190416.models.CreateServiceConfigRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.CreateServiceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstance(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        删除资源组中的节点。目前仅支持删除已经到期的预付费节点，和按量付费节点。

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJob(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        删除任务

        :param request: Request instance for DeleteJob.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteJobRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJob", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceGroup(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        删除资源组

        :param request: Request instance for DeleteResourceGroup.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteResourceGroupRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRsgAsGroup(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        伸缩

        :param request: Request instance for DeleteRsgAsGroup.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteRsgAsGroupRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteRsgAsGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRsgAsGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRsgAsGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRuntime(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        删除运行环境

        :param request: Request instance for DeleteRuntime.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteRuntimeRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteRuntimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRuntime", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuntimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteService(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        删除服务

        :param request: Request instance for DeleteService.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServiceConfig(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        删除服务配置

        :param request: Request instance for DeleteServiceConfig.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceConfigRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DeleteServiceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        获取节点列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceGroups(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        获取资源组列表

        :param request: Request instance for DescribeResourceGroups.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeResourceGroupsRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeResourceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRsgAsGroupActivities(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        查询伸缩组活动

        :param request: Request instance for DescribeRsgAsGroupActivities.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeRsgAsGroupActivitiesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeRsgAsGroupActivitiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRsgAsGroupActivities", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRsgAsGroupActivitiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRsgAsGroups(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        查询资源组的伸缩组信息

        :param request: Request instance for DescribeRsgAsGroups.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeRsgAsGroupsRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeRsgAsGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRsgAsGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRsgAsGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuntimes(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        描述服务运行环境

        :param request: Request instance for DescribeRuntimes.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeRuntimesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeRuntimesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuntimes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuntimesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceConfigs(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        描述服务配置

        :param request: Request instance for DescribeServiceConfigs.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeServiceConfigsRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeServiceConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServices(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        描述服务

        :param request: Request instance for DescribeServices.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DescribeServicesRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DescribeServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServices", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRsgAsGroup(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        停用资源组的伸缩组

        :param request: Request instance for DisableRsgAsGroup.
        :type request: :class:`tencentcloud.tiems.v20190416.models.DisableRsgAsGroupRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.DisableRsgAsGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRsgAsGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRsgAsGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableRsgAsGroup(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        启用资源组的伸缩组

        :param request: Request instance for EnableRsgAsGroup.
        :type request: :class:`tencentcloud.tiems.v20190416.models.EnableRsgAsGroupRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.EnableRsgAsGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableRsgAsGroup", params, headers=headers)
            response = json.loads(body)
            model = models.EnableRsgAsGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExposeService(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        暴露服务

        :param request: Request instance for ExposeService.
        :type request: :class:`tencentcloud.tiems.v20190416.models.ExposeServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.ExposeServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExposeService", params, headers=headers)
            response = json.loads(body)
            model = models.ExposeServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateJob(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        更新任务

        :param request: Request instance for UpdateJob.
        :type request: :class:`tencentcloud.tiems.v20190416.models.UpdateJobRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.UpdateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateJob", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRsgAsGroup(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        更新资源组的伸缩组

        :param request: Request instance for UpdateRsgAsGroup.
        :type request: :class:`tencentcloud.tiems.v20190416.models.UpdateRsgAsGroupRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.UpdateRsgAsGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRsgAsGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRsgAsGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateService(self, request):
        """因业务策略调整，腾讯云TI平台TI-EMS已经于2022年6月30日下线并停止提供服务。若您有新增的业务需求，可前往TI-ONE(https://cloud.tencent.com/document/product/851)使用。

        更新服务

        :param request: Request instance for UpdateService.
        :type request: :class:`tencentcloud.tiems.v20190416.models.UpdateServiceRequest`
        :rtype: :class:`tencentcloud.tiems.v20190416.models.UpdateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateService", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))