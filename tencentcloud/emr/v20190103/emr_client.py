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
from tencentcloud.emr.v20190103 import models


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.tencentcloudapi.com'
    _service = 'emr'


    def AddUsersForUserManager(self, request):
        """该接口支持安装了OpenLdap组件的集群。
        新增用户列表（用户管理）。

        :param request: Request instance for AddUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.AddUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddUsersForUserManagerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInstance(self, request):
        """创建EMR集群实例

        :param request: Request instance for CreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.CreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.CreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstance", params, headers=headers)
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


    def DescribeClusterNodes(self, request):
        """查询集群节点信息

        :param request: Request instance for DescribeClusterNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeClusterNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClusterNodesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCvmQuota(self, request):
        """获取账户的CVM配额

        :param request: Request instance for DescribeCvmQuota.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeCvmQuotaRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeCvmQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCvmQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEmrApplicationStatics(self, request):
        """yarn application 统计接口查询

        :param request: Request instance for DescribeEmrApplicationStatics.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeEmrApplicationStaticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrApplicationStatics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEmrApplicationStaticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceRenewNodes(self, request):
        """预付费集群隔离后续费资源查询

        :param request: Request instance for DescribeInstanceRenewNodes.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstanceRenewNodesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstanceRenewNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceRenewNodes", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceRenewNodesResponse()
                model._deserialize(response["Response"])
                return model
            else:
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
        """查询EMR实例

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
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


    def DescribeInstancesList(self, request):
        """EMR集群实例列表查询

        :param request: Request instance for DescribeInstancesList.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeInstancesListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeJobFlow(self, request):
        """查询流程任务

        :param request: Request instance for DescribeJobFlow.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeJobFlowRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeJobFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobFlow", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeJobFlowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceSchedule(self, request):
        """获取yarn资源调度页面的数据

        :param request: Request instance for DescribeResourceSchedule.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeResourceScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceSchedule", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceScheduleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsersForUserManager(self, request):
        """该接口支持安装了OpenLdap组件的集群。
        批量导出用户。对于kerberos集群，如果需要kertab文件下载地址，可以将NeedKeytabInfo设置为true；注意SupportDownLoadKeyTab为true，但是DownLoadKeyTabUrl为空字符串，表示keytab文件在后台没有准备好（正在生成）。

        :param request: Request instance for DescribeUsersForUserManager.
        :type request: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.DescribeUsersForUserManagerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsersForUserManager", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsersForUserManagerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquirePriceRenewEmr(self, request):
        """集群续费询价。

        :param request: Request instance for InquirePriceRenewEmr.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquirePriceRenewEmrRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquirePriceRenewEmrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenewEmr", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceRenewEmrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateInstance(self, request):
        """创建实例询价

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRenewInstance(self, request):
        """续费询价。

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceScaleOutInstance(self, request):
        """扩容询价. 当扩容时候，请通过该接口查询价格。

        :param request: Request instance for InquiryPriceScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceScaleOutInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceUpdateInstance(self, request):
        """变配询价

        :param request: Request instance for InquiryPriceUpdateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.InquiryPriceUpdateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpdateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpdateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourcePools(self, request):
        """刷新动态资源池

        :param request: Request instance for ModifyResourcePools.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourcePoolsRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourcePoolsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePools", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourcePoolsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourceScheduleConfig(self, request):
        """修改YARN资源调度的资源配置

        :param request: Request instance for ModifyResourceScheduleConfig.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceScheduleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduleConfig", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourceScheduleConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourceScheduler(self, request):
        """修改了yarn的资源调度器，点击部署生效

        :param request: Request instance for ModifyResourceScheduler.
        :type request: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ModifyResourceSchedulerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceScheduler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourceSchedulerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunJobFlow(self, request):
        """创建流程作业

        :param request: Request instance for RunJobFlow.
        :type request: :class:`tencentcloud.emr.v20190103.models.RunJobFlowRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.RunJobFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunJobFlow", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunJobFlowResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScaleOutInstance(self, request):
        """扩容节点

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ScaleOutInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncPodState(self, request):
        """EMR同步TKE中POD状态

        :param request: Request instance for SyncPodState.
        :type request: :class:`tencentcloud.emr.v20190103.models.SyncPodStateRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.SyncPodStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncPodState", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncPodStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateInstance(self, request):
        """销毁EMR实例。此接口仅支持弹性MapReduce正式计费版本。

        :param request: Request instance for TerminateInstance.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstance", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateTasks(self, request):
        """缩容Task节点

        :param request: Request instance for TerminateTasks.
        :type request: :class:`tencentcloud.emr.v20190103.models.TerminateTasksRequest`
        :rtype: :class:`tencentcloud.emr.v20190103.models.TerminateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateTasks", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateTasksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)