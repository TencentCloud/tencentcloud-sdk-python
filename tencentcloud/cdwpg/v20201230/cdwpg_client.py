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
from tencentcloud.cdwpg.v20201230 import models


class CdwpgClient(AbstractClient):
    _apiVersion = '2020-12-30'
    _endpoint = 'cdwpg.tencentcloudapi.com'
    _service = 'cdwpg'


    def CreateInstanceByApi(self, request):
        r"""创建集群

        :param request: Request instance for CreateInstanceByApi.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.CreateInstanceByApiRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.CreateInstanceByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceByApi", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        r"""获取云原生实例对应的账号列表

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBConfigHistory(self, request):
        r"""DescribeDBConfigHistory1

        :param request: Request instance for DescribeDBConfigHistory.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeDBConfigHistoryRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeDBConfigHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBConfigHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBConfigHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBParams(self, request):
        r"""配置描述

        :param request: Request instance for DescribeDBParams.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeDBParamsRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeDBParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeErrorLog(self, request):
        r"""查询错误日志

        :param request: Request instance for DescribeErrorLog.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeErrorLogRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeErrorLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeErrorLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeErrorLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstance(self, request):
        r"""根据实例ID查询某个实例的具体信息

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceInfo(self, request):
        r"""获取集群信息

        :param request: Request instance for DescribeInstanceInfo.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceInfoRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodes(self, request):
        r"""节点list

        :param request: Request instance for DescribeInstanceNodes.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceNodesRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceOperations(self, request):
        r"""在集群详情页面，拉取该集群的操作

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceOperations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceState(self, request):
        r"""集群详情页中显示集群状态、流程进度等

        :param request: Request instance for DescribeInstanceState.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceStateRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""获取云原生实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeInstancesResponse`

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


    def DescribeSimpleInstances(self, request):
        r"""获取集群实例列表

        :param request: Request instance for DescribeSimpleInstances.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeSimpleInstancesRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeSimpleInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSimpleInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSimpleInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLog(self, request):
        r"""查询慢SQL日志

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeSlowLogRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpgradeList(self, request):
        r"""升级记录

        :param request: Request instance for DescribeUpgradeList.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeUpgradeListRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeUpgradeListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpgradeList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpgradeListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserHbaConfig(self, request):
        r"""user_hba

        :param request: Request instance for DescribeUserHbaConfig.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DescribeUserHbaConfigRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DescribeUserHbaConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserHbaConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserHbaConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyInstanceByApi(self, request):
        r"""销毁集群

        :param request: Request instance for DestroyInstanceByApi.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.DestroyInstanceByApiRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.DestroyInstanceByApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstanceByApi", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceByApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBParameters(self, request):
        r"""集群配置下发

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBParameters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""修改实例信息，目前为实例名称

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserHba(self, request):
        r"""修改用户Hba配置

        :param request: Request instance for ModifyUserHba.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ModifyUserHbaRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ModifyUserHbaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserHba", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserHbaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        r"""修改账号密码

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInstance(self, request):
        r"""用户在控制台主动发起重启实例

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.RestartInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleOutInstance(self, request):
        r"""水平扩容

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ScaleUpInstance(self, request):
        r"""控制台垂直变配集群

        :param request: Request instance for ScaleUpInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.ScaleUpInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.ScaleUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        r"""在线升级

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.cdwpg.v20201230.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwpg.v20201230.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))