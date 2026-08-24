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
from tencentcloud.bdrc.v20260330 import models


class BdrcClient(AbstractClient):
    _apiVersion = '2026-03-30'
    _endpoint = 'bdrc.tencentcloudapi.com'
    _service = 'bdrc'


    def ApplyBackupGroup(self, request):
        r"""回滚备份组

        :param request: Request instance for ApplyBackupGroup.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ApplyBackupGroupRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ApplyBackupGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyBackupGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyBackupGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindAutoBackupPolicy(self, request):
        r"""将实例绑定到备份策略上

        :param request: Request instance for BindAutoBackupPolicy.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.BindAutoBackupPolicyRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.BindAutoBackupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindAutoBackupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.BindAutoBackupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoBackupPolicy(self, request):
        r"""创建备份策略

        :param request: Request instance for CreateAutoBackupPolicy.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateAutoBackupPolicyRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateAutoBackupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoBackupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoBackupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupGroup(self, request):
        r"""创建备份组

        :param request: Request instance for CreateBackupGroup.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateBackupGroupRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateBackupGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupVault(self, request):
        r"""创建备份库

        :param request: Request instance for CreateBackupVault.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateBackupVaultRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateBackupVaultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupVault", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupVaultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisasterRecoveryProtectGroup(self, request):
        r"""本接口用于创建容灾保护组

        :param request: Request instance for CreateDisasterRecoveryProtectGroup.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateDisasterRecoveryProtectGroupRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateDisasterRecoveryProtectGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisasterRecoveryProtectGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisasterRecoveryProtectGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisasterRecoverySitePair(self, request):
        r"""创建容灾站点对

        :param request: Request instance for CreateDisasterRecoverySitePair.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateDisasterRecoverySitePairRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateDisasterRecoverySitePairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisasterRecoverySitePair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisasterRecoverySitePairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDisasterRecoveryVpcMapping(self, request):
        r"""本接口用于创建容灾站点VPC网络映射

        :param request: Request instance for CreateDisasterRecoveryVpcMapping.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateDisasterRecoveryVpcMappingRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateDisasterRecoveryVpcMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisasterRecoveryVpcMapping", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisasterRecoveryVpcMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileBackup(self, request):
        r"""本接口用于创建文件备份点

        :param request: Request instance for CreateFileBackup.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateFileBackupRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateFileBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileBackupPlan(self, request):
        r"""本接口用于创建备份计划

        :param request: Request instance for CreateFileBackupPlan.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateFileBackupPlanRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateFileBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFileRestoreTask(self, request):
        r"""创建恢复任务

        :param request: Request instance for CreateFileRestoreTask.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateFileRestoreTaskRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateFileRestoreTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFileRestoreTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFileRestoreTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceCopyPair(self, request):
        r"""本接口用于创建CVM复制对

        :param request: Request instance for CreateInstanceCopyPair.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateInstanceCopyPairRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateInstanceCopyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceCopyPair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceCopyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstanceDrillPairs(self, request):
        r"""创建cvm演练

        :param request: Request instance for CreateInstanceDrillPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateInstanceDrillPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateInstanceDrillPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceDrillPairs", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceDrillPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupMapping(self, request):
        r"""本接口用于为站点对新增安全组映射，生产端实例绑定的安全组为源端，需要为每个生产端实例绑定的安全组建立映射，在创建复制对时，会自动以映射后的目标安全组作为容灾端实例绑定的安全组。

        :param request: Request instance for CreateSecurityGroupMapping.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.CreateSecurityGroupMappingRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.CreateSecurityGroupMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupMapping", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAutoBackupPolicies(self, request):
        r"""删除备份策略

        :param request: Request instance for DeleteAutoBackupPolicies.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteAutoBackupPoliciesRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteAutoBackupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAutoBackupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAutoBackupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupGroups(self, request):
        r"""删除备份组

        :param request: Request instance for DeleteBackupGroups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteBackupGroupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteBackupGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupVaults(self, request):
        r"""删除备份库

        :param request: Request instance for DeleteBackupVaults.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteBackupVaultsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteBackupVaultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupVaults", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupVaultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCopyPairs(self, request):
        r"""本接口用于删除容灾复制对

        :param request: Request instance for DeleteCopyPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteCopyPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteCopyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCopyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCopyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDisasterRecoveryProtectGroups(self, request):
        r"""本接口用于删除容灾保护组

        :param request: Request instance for DeleteDisasterRecoveryProtectGroups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteDisasterRecoveryProtectGroupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteDisasterRecoveryProtectGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDisasterRecoveryProtectGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDisasterRecoveryProtectGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDisasterRecoverySitePairs(self, request):
        r"""删除容灾站点对

        :param request: Request instance for DeleteDisasterRecoverySitePairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteDisasterRecoverySitePairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteDisasterRecoverySitePairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDisasterRecoverySitePairs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDisasterRecoverySitePairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDisasterRecoveryVpcMapping(self, request):
        r"""本接口用于删除容灾站点对vpc映射信息

        :param request: Request instance for DeleteDisasterRecoveryVpcMapping.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteDisasterRecoveryVpcMappingRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteDisasterRecoveryVpcMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDisasterRecoveryVpcMapping", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDisasterRecoveryVpcMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDrillPairs(self, request):
        r"""删除演练对/演练组

        :param request: Request instance for DeleteDrillPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteDrillPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteDrillPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDrillPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDrillPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFileBackupPlans(self, request):
        r"""删除备份计划

        :param request: Request instance for DeleteFileBackupPlans.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteFileBackupPlansRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteFileBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFileBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFileBackups(self, request):
        r"""删除文件备份点

        :param request: Request instance for DeleteFileBackups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteFileBackupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteFileBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFileBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFileBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroupMapping(self, request):
        r"""本接口用于删除站点对已添加的安全组映射

        :param request: Request instance for DeleteSecurityGroupMapping.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DeleteSecurityGroupMappingRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DeleteSecurityGroupMappingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupMapping", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupMappingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoBackupPolicies(self, request):
        r"""查询定期备份策略列表

        :param request: Request instance for DescribeAutoBackupPolicies.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeAutoBackupPoliciesRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeAutoBackupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoBackupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoBackupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupGroupRollbackTasks(self, request):
        r"""查询备份组恢复任务详情

        :param request: Request instance for DescribeBackupGroupRollbackTasks.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupGroupRollbackTasksRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupGroupRollbackTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupGroupRollbackTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupGroupRollbackTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupGroups(self, request):
        r"""查询备份组列表

        :param request: Request instance for DescribeBackupGroups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupGroupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupGroupsDeniedActions(self, request):
        r"""查询操作掩码

        :param request: Request instance for DescribeBackupGroupsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupGroupsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupGroupsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupGroupsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupGroupsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupInstances(self, request):
        r"""本接口用来浏览已有受保护实例列表

        :param request: Request instance for DescribeBackupInstances.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupInstancesRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupOverviewGeneral(self, request):
        r"""查询备份概览信息

        :param request: Request instance for DescribeBackupOverviewGeneral.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupOverviewGeneralRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupOverviewGeneralResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupOverviewGeneral", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupOverviewGeneralResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupPlans(self, request):
        r"""查询整机备份计划

        :param request: Request instance for DescribeBackupPlans.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupPlansRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupVaults(self, request):
        r"""查询备份库信息

        :param request: Request instance for DescribeBackupVaults.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupVaultsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupVaultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupVaults", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupVaultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupVaultsDeniedActions(self, request):
        r"""查询备份库操作掩码

        :param request: Request instance for DescribeBackupVaultsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupVaultsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeBackupVaultsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupVaultsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupVaultsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCommonBackupPoints(self, request):
        r"""查询共同备份点信息

        :param request: Request instance for DescribeCommonBackupPoints.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeCommonBackupPointsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeCommonBackupPointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCommonBackupPoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCommonBackupPointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCopyPairs(self, request):
        r"""本接口用来查询容灾复制对

        :param request: Request instance for DescribeCopyPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeCopyPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeCopyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCopyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCopyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCopyPairsDeniedActions(self, request):
        r"""查询复制对掩码

        :param request: Request instance for DescribeCopyPairsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeCopyPairsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeCopyPairsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCopyPairsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCopyPairsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoveryDrillGroups(self, request):
        r"""本接口用来查询容灾复制对

        :param request: Request instance for DescribeDisasterRecoveryDrillGroups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoveryDrillGroupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoveryDrillGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoveryDrillGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoveryDrillGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoveryOverview(self, request):
        r"""查询容灾资源概览

        :param request: Request instance for DescribeDisasterRecoveryOverview.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoveryOverviewRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoveryOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoveryOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoveryOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoveryProtectGroups(self, request):
        r"""本接口用来查询容灾保护组

        :param request: Request instance for DescribeDisasterRecoveryProtectGroups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoveryProtectGroupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoveryProtectGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoveryProtectGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoveryProtectGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoverySitePairs(self, request):
        r"""本接口用来查询容灾站点对

        :param request: Request instance for DescribeDisasterRecoverySitePairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoverySitePairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoverySitePairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoverySitePairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoverySitePairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoverySitePairsDeniedActions(self, request):
        r"""查询指定容灾站点对当前不允许执行的操作列表（操作掩码）。前端在展示容灾策略操作菜单时，可基于该接口返回结果灰化或屏蔽相应入口，并向用户提示原因（错误码 + 错误信息）。

        :param request: Request instance for DescribeDisasterRecoverySitePairsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoverySitePairsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoverySitePairsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoverySitePairsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoverySitePairsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisasterRecoverySupportRegion(self, request):
        r"""查询当前地域支持容灾的生产地域配置列表

        :param request: Request instance for DescribeDisasterRecoverySupportRegion.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoverySupportRegionRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisasterRecoverySupportRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisasterRecoverySupportRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisasterRecoverySupportRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDisks(self, request):
        r"""本接口用来查询容灾云硬盘的详情，如系统盘的镜像格式。

        :param request: Request instance for DescribeDisks.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisksRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrillPairs(self, request):
        r"""查询演练对列表

        :param request: Request instance for DescribeDrillPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDrillPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDrillPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrillPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrillPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDrillPairsDeniedActions(self, request):
        r"""查询演练操作掩码

        :param request: Request instance for DescribeDrillPairsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeDrillPairsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeDrillPairsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDrillPairsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDrillPairsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileBackupObjects(self, request):
        r"""本接口用来浏览已有备份目录/文件内容

        :param request: Request instance for DescribeFileBackupObjects.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupObjectsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileBackupObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileBackupObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileBackupPlans(self, request):
        r"""本接口用来浏览已有备份计划内容

        :param request: Request instance for DescribeFileBackupPlans.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupPlansRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileBackups(self, request):
        r"""本接口用来浏览已有备份点详情

        :param request: Request instance for DescribeFileBackups.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileBackupsDeniedActions(self, request):
        r"""本接口用来查询备份操作掩码

        :param request: Request instance for DescribeFileBackupsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileBackupsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileBackupsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileBackupsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileRestoreTasks(self, request):
        r"""查询备份恢复任务列表

        :param request: Request instance for DescribeFileRestoreTasks.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileRestoreTasksRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeFileRestoreTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileRestoreTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileRestoreTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeJobs(self, request):
        r"""本接口用于Agent查询相关Agent任务信息

        :param request: Request instance for DescribeJobs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeJobsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePriceCreateCopyPairs(self, request):
        r"""本接口（DescribePriceCreateCopyPairs）用于查询创建容灾复制对的价格。支持批量询价，入参为每个复制对的盘容量数组，返回与入参一一对应的后付费每小时价格。

        :param request: Request instance for DescribePriceCreateCopyPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribePriceCreateCopyPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribePriceCreateCopyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePriceCreateCopyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePriceCreateCopyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectGroupsDeniedActions(self, request):
        r"""查询保护组操作掩码

        :param request: Request instance for DescribeProtectGroupsDeniedActions.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeProtectGroupsDeniedActionsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeProtectGroupsDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectGroupsDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectGroupsDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectedInstances(self, request):
        r"""本接口用来浏览已有受保护实例列表

        :param request: Request instance for DescribeProtectedInstances.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeProtectedInstancesRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeProtectedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupMappings(self, request):
        r"""本接口用于查询安全组映射列表

        :param request: Request instance for DescribeSecurityGroupMappings.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeSecurityGroupMappingsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeSecurityGroupMappingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupMappings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupMappingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcMappings(self, request):
        r"""本接口用来查询站点对的vpc映射信息

        :param request: Request instance for DescribeVpcMappings.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.DescribeVpcMappingsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.DescribeVpcMappingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcMappings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcMappingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FinishFailoverCopyPairs(self, request):
        r"""完成切换

        :param request: Request instance for FinishFailoverCopyPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.FinishFailoverCopyPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.FinishFailoverCopyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FinishFailoverCopyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.FinishFailoverCopyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoBackupPolicyAttribute(self, request):
        r"""修改备份策略

        :param request: Request instance for ModifyAutoBackupPolicyAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyAutoBackupPolicyAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyAutoBackupPolicyAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoBackupPolicyAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoBackupPolicyAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupAttribute(self, request):
        r"""删除备份组

        :param request: Request instance for ModifyBackupAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyBackupAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyBackupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupVaultAttribute(self, request):
        r"""修改备份库信息

        :param request: Request instance for ModifyBackupVaultAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyBackupVaultAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyBackupVaultAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupVaultAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupVaultAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCopyPairAttribute(self, request):
        r"""修改容灾复制对

        :param request: Request instance for ModifyCopyPairAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyCopyPairAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyCopyPairAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCopyPairAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCopyPairAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDrillGroupAttribute(self, request):
        r"""修改演练组

        :param request: Request instance for ModifyDrillGroupAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyDrillGroupAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyDrillGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDrillGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDrillGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDrillPairAttribute(self, request):
        r"""修改演练

        :param request: Request instance for ModifyDrillPairAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyDrillPairAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyDrillPairAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDrillPairAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDrillPairAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileBackupAttribute(self, request):
        r"""修改文件备份信息

        :param request: Request instance for ModifyFileBackupAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyFileBackupAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyFileBackupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileBackupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileBackupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFileBackupPlan(self, request):
        r"""本接口用于修改已有的备份计划配置

        :param request: Request instance for ModifyFileBackupPlan.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyFileBackupPlanRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyFileBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFileBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFileBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProtectGroupAttribute(self, request):
        r"""修改容灾保护组

        :param request: Request instance for ModifyProtectGroupAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifyProtectGroupAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifyProtectGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProtectGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProtectGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySitePairAttribute(self, request):
        r"""修改容灾站点对

        :param request: Request instance for ModifySitePairAttribute.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ModifySitePairAttributeRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ModifySitePairAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySitePairAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySitePairAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportAgentMetrics(self, request):
        r"""本接口用于上报Agent指标信息

        :param request: Request instance for ReportAgentMetrics.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ReportAgentMetricsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ReportAgentMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportAgentMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.ReportAgentMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportGatewayHeartbeat(self, request):
        r"""本接口用于Agent心跳上报

        :param request: Request instance for ReportGatewayHeartbeat.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ReportGatewayHeartbeatRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ReportGatewayHeartbeatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportGatewayHeartbeat", params, headers=headers)
            response = json.loads(body)
            model = models.ReportGatewayHeartbeatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReportJobProgress(self, request):
        r"""本接口用于上报Agent任务信息

        :param request: Request instance for ReportJobProgress.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.ReportJobProgressRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.ReportJobProgressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportJobProgress", params, headers=headers)
            response = json.loads(body)
            model = models.ReportJobProgressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunCopyPairTasks(self, request):
        r"""启动复制对

        :param request: Request instance for RunCopyPairTasks.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.RunCopyPairTasksRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.RunCopyPairTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunCopyPairTasks", params, headers=headers)
            response = json.loads(body)
            model = models.RunCopyPairTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunFailoverCopyPairs(self, request):
        r"""故障切换

        :param request: Request instance for RunFailoverCopyPairs.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.RunFailoverCopyPairsRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.RunFailoverCopyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunFailoverCopyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.RunFailoverCopyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunInstancesWithBackupGroup(self, request):
        r"""备份组新建云服务器

        :param request: Request instance for RunInstancesWithBackupGroup.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.RunInstancesWithBackupGroupRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.RunInstancesWithBackupGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunInstancesWithBackupGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RunInstancesWithBackupGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCopyPairTasks(self, request):
        r"""停止复制对

        :param request: Request instance for StopCopyPairTasks.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.StopCopyPairTasksRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.StopCopyPairTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCopyPairTasks", params, headers=headers)
            response = json.loads(body)
            model = models.StopCopyPairTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindAutoBackupPolicy(self, request):
        r"""将实例从备份策略上解绑

        :param request: Request instance for UnbindAutoBackupPolicy.
        :type request: :class:`tencentcloud.bdrc.v20260330.models.UnbindAutoBackupPolicyRequest`
        :rtype: :class:`tencentcloud.bdrc.v20260330.models.UnbindAutoBackupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindAutoBackupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindAutoBackupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))