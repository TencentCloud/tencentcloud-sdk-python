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
from tencentcloud.lighthouse.v20200324 import models


class LighthouseClient(AbstractClient):
    _apiVersion = '2020-03-24'
    _endpoint = 'lighthouse.tencentcloudapi.com'
    _service = 'lighthouse'


    def CreateFirewallRules(self, request):
        """本接口（CreateFirewallRules）用于在实例上添加防火墙规则。

        * Protocol 字段支持输入 TCP，UDP，或 ALL。

        * Port 字段允许输入 ALL，或者一个单独的端口号，或者用逗号分隔的离散端口号，或者用减号分隔的两个端口号代表的端口范围。当 Port 为范围时，减号分隔的第一个端口号小于第二个端口号。当 Protocol 字段不是 TCP 或 UDP 时，Port 字段只能为空或 ALL。Port 字段长度不得超过 64。

        :param request: Request instance for CreateFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.CreateFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFirewallRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFirewallRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFirewallRules(self, request):
        """本接口（DeleteFirewallRules）用于删除实例的防火墙规则。

        * Protocol 字段支持输入 TCP，UDP，或 ALL。

        * Port 字段允许输入 ALL，或者一个单独的端口号，或者用逗号分隔的离散端口号，或者用减号分隔的两个端口号代表的端口范围。当 Port 为范围时，减号分隔的第一个端口号小于第二个端口号。当 Protocol 字段不是 TCP 或 UDP 时，Port 字段只能为空或 ALL。Port 字段长度不得超过 64。

        :param request: Request instance for DeleteFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DeleteFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFirewallRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFirewallRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBlueprints(self, request):
        """本接口（DescribeBlueprints）用于查询镜像信息。

        :param request: Request instance for DescribeBlueprints.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintsRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBlueprintsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBlueprints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBlueprintsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBundles(self, request):
        """本接口（DescribeBundles）用于查询套餐信息。

        :param request: Request instance for DescribeBundles.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundlesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeBundlesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBundles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBundlesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFirewallRules(self, request):
        """本接口（DescribeFirewallRules）用于查询实例的防火墙规则。

        :param request: Request instance for DescribeFirewallRules.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeFirewallRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFirewallRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFirewallRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """本接口（DescribeInstances）用于查询一个或多个实例的详细信息。

        * 可以根据实例 ID、实例名称或者实例的内网 IP 查询实例的详细信息。
        * 过滤信息详细请见过滤器 [Filters](https://cloud.tencent.com/document/product/1207/47576#Filter) 。
        * 如果参数为空，返回当前用户一定数量（Limit 所指定的数量，默认为 20）的实例。
        * 支持查询实例的最新操作（LatestOperation）以及最新操作状态（LatestOperationState）。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesResponse`

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


    def DescribeInstancesTrafficPackages(self, request):
        """本接口（DescribeInstancesTrafficPackages）用于查询一个或多个实例的流量包详情。

        :param request: Request instance for DescribeInstancesTrafficPackages.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.DescribeInstancesTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesTrafficPackages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesTrafficPackagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RebootInstances(self, request):
        """本接口（RebootInstances）用于重启实例。

        * 只有状态为 RUNNING 的实例才可以进行此操作。
        * 接口调用成功时，实例会进入 REBOOTING 状态；重启实例成功时，实例会进入 RUNNING 状态。
        * 支持批量操作，每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebootInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebootInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetInstance(self, request):
        """本接口（ResetInstance）用于重装指定实例上的镜像。

        * 如果指定了 BlueprintId 参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装。
        * 系统盘将会被格式化，并重置；请确保系统盘中无重要文件。
        * 目前不支持实例使用该接口实现 LINUX_UNIX 和 WINDOWS 操作系统切换。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for ResetInstance.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstanceRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.ResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartInstances(self, request):
        """本接口（StartInstances）用于启动一个或多个实例。

        * 只有状态为 STOPPED 的实例才可以进行此操作。
        * 接口调用成功时，实例会进入 STARTING 状态；启动实例成功时，实例会进入 RUNNING 状态。
        * 支持批量操作。每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopInstances(self, request):
        """本接口（StopInstances）用于关闭一个或多个实例。
        * 只有状态为 RUNNING 的实例才可以进行此操作。
        * 接口调用成功时，实例会进入 STOPPING 状态；关闭实例成功时，实例会进入 STOPPED 状态。
        * 支持批量操作。每次请求批量实例的上限为 100。
        * 本接口为异步接口，请求发送成功后会返回一个 RequestId，此时操作并未立即完成。实例操作结果可以通过调用 DescribeInstances 接口查询，如果实例的最新操作状态（LatestOperationState）为“SUCCESS”，则代表操作成功。

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.lighthouse.v20200324.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.lighthouse.v20200324.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)