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
from tencentcloud.es.v20180416 import models


class EsClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'es.tencentcloudapi.com'


    def CreateInstance(self, request):
        """创建指定规格的ES集群实例

        :param request: 调用CreateInstance所需参数的结构体。
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

        :param request: 调用DeleteInstance所需参数的结构体。
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

        :param request: 调用DescribeInstanceLogs所需参数的结构体。
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

        :param request: 调用DescribeInstanceOperations所需参数的结构体。
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

        :param request: 调用DescribeInstances所需参数的结构体。
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


    def RestartInstance(self, request):
        """重启ES集群实例(用于系统版本更新等操作)

        :param request: 调用RestartInstance所需参数的结构体。
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


    def UpdateInstance(self, request):
        """对集群进行扩缩容，修改实例名称，修改配置，重置密码， 添加Kibana黑白名单等操作。参数中InstanceId为必传参数，ForceRestart为选填参数，剩余参数传递组合及含义如下：<br>
          InstanceName：修改实例名称(仅用于标识实例)<br>
          NodeNum：集群数据节点横向扩缩容<br>
          NodeType, DiskSize：集群数据节点纵向扩缩容<br>
          MasterNodeNum: 集群专用主节点横向扩缩容<br>
          MasterNodeType, MasterNodeDiskSize: 集群专用主节点纵向扩缩容<br>
          EsConfig：修改集群配置<br>
          Password：修改集群密码<br>
          EsAcl：修改Kibana密码<br>
          CosBackUp: 设置集群COS自动备份信息<br>
        以上参数组合只能传递一种，多传或少传均会导致请求失败<br>

        :param request: 调用UpdateInstance所需参数的结构体。
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