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
from tencentcloud.keewidb.v20220308 import models


class KeewidbClient(AbstractClient):
    _apiVersion = '2022-03-08'
    _endpoint = 'keewidb.tencentcloudapi.com'
    _service = 'keewidb'


    def AssociateSecurityGroups(self, request):
        r"""本接口 (AssociateSecurityGroups) 用于安全组批量绑定多个指定实例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChangeInstanceMaster(self, request):
        r"""本接口（ChangeInstanceMaster）用于将副本节点提升为主节点。

        :param request: Request instance for ChangeInstanceMaster.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ChangeInstanceMasterRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ChangeInstanceMasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeInstanceMaster", params, headers=headers)
            response = json.loads(body)
            model = models.ChangeInstanceMasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CleanUpInstance(self, request):
        r"""本接口（CleanUpInstance）用于立即下线回收站已隔离的实例。

        :param request: Request instance for CleanUpInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.CleanUpInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.CleanUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CleanUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CleanUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearInstance(self, request):
        r"""本接口（ClearInstance）用于清空实例数据。
        > **说明**：在清空数据流程中，系统将自动进行数据备份，耗时较长，请您耐心等待并提前做好时间规划。

        :param request: Request instance for ClearInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ClearInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ClearInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ClearInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupManually(self, request):
        r"""手动发起备份

        :param request: Request instance for CreateBackupManually.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.CreateBackupManuallyRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.CreateBackupManuallyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupManually", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupManuallyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstances(self, request):
        r"""创建数据库实例

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoBackupConfig(self, request):
        r"""本接口（DescribeAutoBackupConfig）用于获取自动备份配置。

        :param request: Request instance for DescribeAutoBackupConfig.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConnectionConfig(self, request):
        r"""本接口（DescribeConnectionConfig）用于查询实例连接配置，包括出流量和入流量带宽、最大连接数限制。

        :param request: Request instance for DescribeConnectionConfig.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeConnectionConfigRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeConnectionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConnectionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConnectionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        r"""本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceBackups(self, request):
        r"""本接口（DescribeInstanceBackups）用于查询实例全量备份列表。

        :param request: Request instance for DescribeInstanceBackups.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceBackupsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceBinlogs(self, request):
        r"""本接口（DescribeInstanceBinlogs）用于查询增量备份列表。

        :param request: Request instance for DescribeInstanceBinlogs.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceBinlogsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceBinlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceBinlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceBinlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDealDetail(self, request):
        r"""本接口（DescribeInstanceDealDetail）用于查询预付费订单信息。

        :param request: Request instance for DescribeInstanceDealDetail.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceDealDetailRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceDealDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDealDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDealDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodeInfo(self, request):
        r"""本接口（DescribeInstanceNodeInfo）查询实例节点信息。

        :param request: Request instance for DescribeInstanceNodeInfo.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        r"""本接口（DescribeInstanceParamRecords）查询参数配置修改历史列表。

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParamRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        r"""本接口（DescribeInstanceParams）用于查询实例的参数列表。

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceReplicas(self, request):
        r"""本接口（DescribeInstanceReplicas）用于获取实例副本节点信息。

        :param request: Request instance for DescribeInstanceReplicas.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceReplicasRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstanceReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceReplicas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceReplicasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        r"""本接口（DescribeInstances）可以根据地域、网络、实例id、标签、计费方式等条件，搜索查询实例列表。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeInstancesResponse`

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


    def DescribeMaintenanceWindow(self, request):
        r"""本接口（DescribeMaintenanceWindow）用于查询实例维护时间窗。

        :param request: Request instance for DescribeMaintenanceWindow.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductInfo(self, request):
        r"""本接口查询指定可用区和实例类型下keewidb 的售卖规格， 如果用户不在购买白名单中，将不能查询该可用区或该类型的售卖规格详情。申请购买某地域白名单可以提交工单

        :param request: Request instance for DescribeProductInfo.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeProductInfoRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeProductInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        r"""本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySlowLog(self, request):
        r"""本接口（DescribeProxySlowLog）用于查询代理（Proxy）慢日志。

        :param request: Request instance for DescribeProxySlowLog.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeProxySlowLogRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeProxySlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskInfo(self, request):
        r"""本接口（DescribeTaskInfo）用于查询异步任务结果。

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskList(self, request):
        r"""本接口（DescribeTaskList）用于查询任务列表信息。

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTendisSlowLog(self, request):
        r"""本接口（DescribeTendisSlowLog）用于查询实例慢日志。

        :param request: Request instance for DescribeTendisSlowLog.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DescribeTendisSlowLogRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DescribeTendisSlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTendisSlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTendisSlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPostpaidInstance(self, request):
        r"""本接口（DestroyPostpaidInstance）用于退还按量计费实例。

        :param request: Request instance for DestroyPostpaidInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DestroyPostpaidInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DestroyPostpaidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPostpaidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPostpaidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyPrepaidInstance(self, request):
        r"""本接口（DestroyPrepaidInstance）用于退还包年包月计费实例。

        :param request: Request instance for DestroyPrepaidInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DestroyPrepaidInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DestroyPrepaidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyPrepaidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyPrepaidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        r"""本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoBackupConfig(self, request):
        r"""本接口（ModifyAutoBackupConfig）用于修改自动备份配置。

        :param request: Request instance for ModifyAutoBackupConfig.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConnectionConfig(self, request):
        r"""本接口（ModifyConnectionConfig）用于修改实例的连接配置，包括带宽和最大连接数。

        :param request: Request instance for ModifyConnectionConfig.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyConnectionConfigRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyConnectionConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConnectionConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConnectionConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        r"""本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstance(self, request):
        r"""本接口（ModifyInstance）用于修改实例相关信息。

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyInstanceResponse`

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


    def ModifyInstanceParams(self, request):
        r"""本接口（ModifyInstanceParams）用于修改实例参数配置。

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyInstanceParamsRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaintenanceWindow(self, request):
        r"""本接口（ModifyMaintenanceWindow）修改实例维护时间窗时间。

        :param request: Request instance for ModifyMaintenanceWindow.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkConfig(self, request):
        r"""本接口（ModifyNetworkConfig）用于修改实例网络配置。

        :param request: Request instance for ModifyNetworkConfig.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ModifyNetworkConfigRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ModifyNetworkConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstance(self, request):
        r"""本接口（RenewInstance）用于为包年包月计费实例续费。

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetPassword(self, request):
        r"""本接口（ResetPassword）用于重置数据库访问密码。

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartUpInstance(self, request):
        r"""本接口（StartUpInstance）用于按量计费实例解隔离

        :param request: Request instance for StartUpInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.StartUpInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.StartUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StartUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        r"""本接口（UpgradeInstance）用于对实例进行配置变更。

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.keewidb.v20220308.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.keewidb.v20220308.models.UpgradeInstanceResponse`

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