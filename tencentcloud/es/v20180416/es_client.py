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
from tencentcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.tencentcloudapi.com'
    _service = 'es'


    def CreateInstance(self, request):
        """创建指定规格的ES集群实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteInstance(self, request):
        """销毁集群实例

        :param request: Request instance for DeleteInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DeleteInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DeleteInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """查询用户该地域下符合条件的ES集群的日志

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceLogs", params)
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


    def DescribeInstanceOperations(self, request):
        """查询实例指定条件下的操作记录

        :param request: Request instance for DescribeInstanceOperations.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstanceOperationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceOperations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceOperationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstances(self, request):
        """查询用户该地域下符合条件的所有实例

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """查询集群各视图数据，包括集群维度、节点维度、Kibana维度

        :param request: Request instance for DescribeViews.
        :type request: :class:`tencentcloud.es.v20180416.models.DescribeViewsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DescribeViewsResponse`

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


    def DiagnoseInstance(self, request):
        """智能运维诊断集群

        :param request: Request instance for DiagnoseInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.DiagnoseInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.DiagnoseInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DiagnoseInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DiagnoseInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetRequestTargetNodeTypes(self, request):
        """获取接收客户端请求的节点类型

        :param request: Request instance for GetRequestTargetNodeTypes.
        :type request: :class:`tencentcloud.es.v20180416.models.GetRequestTargetNodeTypesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.GetRequestTargetNodeTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetRequestTargetNodeTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetRequestTargetNodeTypesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartInstance(self, request):
        """重启ES集群实例(用于系统版本更新等操作)

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartKibana(self, request):
        """重启Kibana

        :param request: Request instance for RestartKibana.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartKibanaRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartKibanaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartKibana", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartKibanaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartNodes(self, request):
        """用于重启集群节点

        :param request: Request instance for RestartNodes.
        :type request: :class:`tencentcloud.es.v20180416.models.RestartNodesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.RestartNodesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartNodes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartNodesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateDiagnoseSettings(self, request):
        """更新智能运维配置

        :param request: Request instance for UpdateDiagnoseSettings.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateDiagnoseSettingsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateDiagnoseSettingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateDiagnoseSettings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDiagnoseSettingsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateInstance(self, request):
        """对集群进行节点规格变更，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作。参数中InstanceId为必传参数，ForceRestart为选填参数，剩余参数传递组合及含义如下：
        - InstanceName：修改实例名称(仅用于标识实例)
        - NodeInfoList: 修改节点配置（节点横向扩缩容，纵向扩缩容，增加主节点，增加冷节点等）
        - EsConfig：修改集群配置
        - Password：修改默认用户elastic的密码
        - EsAcl：修改访问控制列表
        - CosBackUp: 设置集群COS自动备份信息
        以上参数组合只能传递一种，多传或少传均会导致请求失败

        :param request: Request instance for UpdateInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateJdk(self, request):
        """更新实例Jdk配置

        :param request: Request instance for UpdateJdk.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateJdkRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateJdkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateJdk", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateJdkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdatePlugins(self, request):
        """变更插件列表

        :param request: Request instance for UpdatePlugins.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdatePluginsRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdatePluginsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdatePlugins", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdatePluginsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRequestTargetNodeTypes(self, request):
        """更新接收客户端请求的节点类型

        :param request: Request instance for UpdateRequestTargetNodeTypes.
        :type request: :class:`tencentcloud.es.v20180416.models.UpdateRequestTargetNodeTypesRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpdateRequestTargetNodeTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRequestTargetNodeTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRequestTargetNodeTypesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeInstance(self, request):
        """升级ES集群版本

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeLicense(self, request):
        """升级ES商业特性

        :param request: Request instance for UpgradeLicense.
        :type request: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseRequest`
        :rtype: :class:`tencentcloud.es.v20180416.models.UpgradeLicenseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeLicense", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeLicenseResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)