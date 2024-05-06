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
from tencentcloud.cdb.v20170320 import models


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.tencentcloudapi.com'
    _service = 'cdb'


    def AddTimeWindow(self, request):
        """本接口(AddTimeWindow)用于添加云数据库实例的维护时间窗口，以指定实例在哪些时间段可以自动执行切换访问操作。

        :param request: Request instance for AddTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AddTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AddTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.AddTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustCdbProxy(self, request):
        """调整数据库代理配置

        :param request: Request instance for AdjustCdbProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustCdbProxy", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustCdbProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustCdbProxyAddress(self, request):
        """调整数据库代理地址配置

        :param request: Request instance for AdjustCdbProxyAddress.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyAddressRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AdjustCdbProxyAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustCdbProxyAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustCdbProxyAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AnalyzeAuditLogs(self, request):
        """在不同过滤条件下的审计日志结果集中，选定特定的数据列进行聚合统计。

        :param request: Request instance for AnalyzeAuditLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AnalyzeAuditLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AnalyzeAuditLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AnalyzeAuditLogs", params, headers=headers)
            response = json.loads(body)
            model = models.AnalyzeAuditLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """本接口(AssociateSecurityGroups)用于安全组批量绑定实例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AssociateSecurityGroupsResponse`

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


    def BalanceRoGroupLoad(self, request):
        """本接口(BalanceRoGroupLoad)用于重新均衡 RO 组内实例的负载。注意，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库，谨慎操作。

        :param request: Request instance for BalanceRoGroupLoad.
        :type request: :class:`tencentcloud.cdb.v20170320.models.BalanceRoGroupLoadRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.BalanceRoGroupLoadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BalanceRoGroupLoad", params, headers=headers)
            response = json.loads(body)
            model = models.BalanceRoGroupLoadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckMigrateCluster(self, request):
        """高可用实例一键迁移到集群版校验

        :param request: Request instance for CheckMigrateCluster.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CheckMigrateClusterRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CheckMigrateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckMigrateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CheckMigrateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAuditService(self, request):
        """实例关闭审计服务

        :param request: Request instance for CloseAuditService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseAuditServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseCDBProxy(self, request):
        """关闭数据库代理

        :param request: Request instance for CloseCDBProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseCDBProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseCDBProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseCDBProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CloseCDBProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseCdbProxyAddress(self, request):
        """请求关闭数据库代理地址

        :param request: Request instance for CloseCdbProxyAddress.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseCdbProxyAddressRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseCdbProxyAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseCdbProxyAddress", params, headers=headers)
            response = json.loads(body)
            model = models.CloseCdbProxyAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseSSL(self, request):
        """关闭SSL连接功能。

        :param request: Request instance for CloseSSL.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseSSLRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseSSL", params, headers=headers)
            response = json.loads(body)
            model = models.CloseSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWanService(self, request):
        """本接口(CloseWanService)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问。

        :param request: Request instance for CloseWanService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseWanServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseWanServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseWanService", params, headers=headers)
            response = json.loads(body)
            model = models.CloseWanServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccounts(self, request):
        """本接口(CreateAccounts)用于创建云数据库的账户，需要指定新的账户名和域名，以及所对应的密码，同时可以设置账号的备注信息以及最大可用连接数。

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditLogFile(self, request):
        """本接口(CreateAuditLogFile)用于创建云数据库实例的审计日志文件。

        :param request: Request instance for CreateAuditLogFile.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditLogFileRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditPolicy(self, request):
        """本接口(CreateAuditPolicy)用于创建云数据库实例的审计策略，即将审计规则绑定到具体的云数据库实例上。

        :param request: Request instance for CreateAuditPolicy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditPolicyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditRule(self, request):
        """本接口(CreateAuditRule)用于创建用户在当前地域的审计规则。

        :param request: Request instance for CreateAuditRule.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditRuleRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAuditRuleTemplate(self, request):
        """创建审计规则模板

        :param request: Request instance for CreateAuditRuleTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAuditRuleTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAuditRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAuditRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAuditRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        """本接口(CreateBackup)用于创建数据库备份。

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdbProxy(self, request):
        """主实例创建数据库代理

        :param request: Request instance for CreateCdbProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdbProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdbProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdbProxyAddress(self, request):
        """数据库代理增加代理地址

        :param request: Request instance for CreateCdbProxyAddress.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyAddressRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateCdbProxyAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdbProxyAddress", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdbProxyAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloneInstance(self, request):
        """本接口(CreateCloneInstance) 用于从目标源实例创建一个克隆实例，可以指定克隆实例回档到源实例的指定物理备份文件或者指定的回档时间点。

        :param request: Request instance for CreateCloneInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateCloneInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateCloneInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloneInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloneInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBImportJob(self, request):
        """本接口(CreateDBImportJob)用于创建云数据库数据导入任务。

        注意，用户进行数据导入任务的文件，必须提前上传到腾讯云。用户须在控制台进行文件导入。

        :param request: Request instance for CreateDBImportJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBImportJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBImportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBImportJob", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBImportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstance(self, request):
        """本接口(CreateDBInstance)用于创建包年包月的云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、MySQL 版本号、购买时长和数量等信息创建云数据库实例。

        该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为1，且 TaskStatus 为0，表示实例已经发货成功。

        1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL 5.5 、 MySQL 5.6 、 MySQL 5.7 、 MySQL 8.0 版本；
        4. 支持创建主实例、只读实例、灾备实例；
        5. 当入参指定 Port 和 ParamTemplateType 参数模板，相关参数才会自动初始化（不支持基础版实例）；
        6. 当入参指定 ParamTemplateId 或 AlarmPolicyList 时，需将SDK提升至最新版本方可支持；

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstanceHour(self, request):
        """本接口(CreateDBInstanceHour)用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。

        该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为 1，且 TaskStatus 为 0，表示实例已经发货成功。

        1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL 5.5、MySQL 5.6 、MySQL 5.7 和 MySQL 8.0 版本；
        4. 支持创建主实例、灾备实例和只读实例；
        5. 当入参指定 Port，ParamTemplateType 或 Password 时，该实例会进行初始化操作；

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceHour", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceHourResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatabase(self, request):
        """本接口(CreateDatabase)用于在云数据库实例中创建数据库。

        :param request: Request instance for CreateDatabase.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDatabaseRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDeployGroup(self, request):
        """本接口(CreateDeployGroup)用于创建放置实例的置放群组

        :param request: Request instance for CreateDeployGroup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDeployGroupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDeployGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDeployGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDeployGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateParamTemplate(self, request):
        """该接口（CreateParamTemplate）用于创建参数模板，全地域公共参数Region均为ap-guangzhou。

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoInstanceIp(self, request):
        """本接口(CreateRoInstanceIp)用于创建云数据库只读实例的独立VIP。

        :param request: Request instance for CreateRoInstanceIp.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateRoInstanceIpRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateRoInstanceIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoInstanceIp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoInstanceIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccounts(self, request):
        """本接口(DeleteAccounts)用于删除云数据库的账户。

        :param request: Request instance for DeleteAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditLogFile(self, request):
        """本接口(DeleteAuditLogFile)用于删除云数据库实例的审计日志文件。

        :param request: Request instance for DeleteAuditLogFile.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditLogFileRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditLogFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditLogFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditLogFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditPolicy(self, request):
        """本接口(DeleteAuditPolicy)用于删除用户的审计策略。

        :param request: Request instance for DeleteAuditPolicy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditPolicyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditRule(self, request):
        """本接口(DeleteAuditRule)用于删除用户的审计规则。

        :param request: Request instance for DeleteAuditRule.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditRuleRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAuditRuleTemplates(self, request):
        """删除审计规则模板

        :param request: Request instance for DeleteAuditRuleTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackup(self, request):
        """本接口(DeleteBackup)用于删除数据库备份。本接口只支持删除手动发起的备份。

        :param request: Request instance for DeleteBackup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteBackupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDatabase(self, request):
        """本接口(DeleteDatabase)用于在云数据库实例中删除数据库。

        :param request: Request instance for DeleteDatabase.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteDatabaseRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeployGroups(self, request):
        """根据置放群组ID删除置放群组（置放群组中有资源存在时不能删除该置放群组）

        :param request: Request instance for DeleteDeployGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteDeployGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteDeployGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeployGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeployGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParamTemplate(self, request):
        """该接口（DeleteParamTemplate）用于删除参数模板，全地域公共参数Region均为ap-guangzhou。

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTimeWindow(self, request):
        """本接口(DeleteTimeWindow)用于删除云数据库实例的维护时间窗口。删除实例维护时间窗口之后，默认的维护时间窗为 03:00-04:00，即当选择在维护时间窗口内切换访问新实例时，默认会在 03:00-04:00 点进行切换访问新实例。

        :param request: Request instance for DeleteTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivileges(self, request):
        """本接口(DescribeAccountPrivileges)用于查询云数据库账户支持的权限信息。

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """本接口(DescribeAccounts)用于查询云数据库的所有账户信息。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountsResponse`

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


    def DescribeAsyncRequestInfo(self, request):
        """本接口(DescribeAsyncRequestInfo)用于查询云数据库实例异步任务的执行结果。

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncRequestInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncRequestInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditConfig(self, request):
        """本接口(DescribeAuditConfig)用于查询云数据库审计策略的服务配置，包括审计日志保存时长等。

        :param request: Request instance for DescribeAuditConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditInstanceList(self, request):
        """获取审计实例列表

        :param request: Request instance for DescribeAuditInstanceList.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditInstanceListRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLogFiles(self, request):
        """本接口(DescribeAuditLogFiles)用于查询云数据库实例的审计日志文件。

        :param request: Request instance for DescribeAuditLogFiles.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogFilesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLogFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditLogs(self, request):
        """本接口(DescribeAuditLogs)用于查询数据库审计日志。

        :param request: Request instance for DescribeAuditLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditPolicies(self, request):
        """本接口(DescribeAuditPolicies)用于查询云数据库实例的审计策略。

        :param request: Request instance for DescribeAuditPolicies.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditPoliciesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRuleTemplateModifyHistory(self, request):
        """查询规则模板变更记录

        :param request: Request instance for DescribeAuditRuleTemplateModifyHistory.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplateModifyHistoryRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplateModifyHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleTemplateModifyHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleTemplateModifyHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRuleTemplates(self, request):
        """查询审计规则模板信息

        :param request: Request instance for DescribeAuditRuleTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAuditRules(self, request):
        """本接口(DescribeAuditRules)用于查询用户在当前地域的审计规则。

        :param request: Request instance for DescribeAuditRules.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRulesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAuditRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupConfig(self, request):
        """本接口(DescribeBackupConfig)用于查询数据库备份配置信息。

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDecryptionKey(self, request):
        """本接口(DescribeBackupDecryptionKey)用于查询备份文件解密密钥。

        :param request: Request instance for DescribeBackupDecryptionKey.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDecryptionKeyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDecryptionKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDecryptionKey", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDecryptionKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadRestriction(self, request):
        """该接口用户查询当前地域用户设置的默认备份下载来源限制。

        :param request: Request instance for DescribeBackupDownloadRestriction.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupEncryptionStatus(self, request):
        """本接口(DescribeBackupEncryptionStatus)用于查询实例默认备份加密状态。

        :param request: Request instance for DescribeBackupEncryptionStatus.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupEncryptionStatusRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupEncryptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupEncryptionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupEncryptionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupOverview(self, request):
        """本接口(DescribeBackupOverview)用于查询用户的备份概览。返回用户当前备份总个数、备份总的占用容量、赠送的免费容量、计费容量（容量单位为字节）。

        :param request: Request instance for DescribeBackupOverview.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupOverviewRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupSummaries(self, request):
        """本接口(DescribeBackupSummaries)用于查询备份的统计情况，返回以实例为维度的备份占用容量，以及每个实例的数据备份和日志备份的个数和容量（容量单位为字节）。

        :param request: Request instance for DescribeBackupSummaries.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupSummariesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupSummariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupSummaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupSummariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackups(self, request):
        """本接口(DescribeBackups)用于查询云数据库实例的备份数据。

        :param request: Request instance for DescribeBackups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogBackupOverview(self, request):
        """本接口(DescribeBinlogBackupOverview)用于查询用户在当前地域总的日志备份概览。

        :param request: Request instance for DescribeBinlogBackupOverview.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogBackupOverviewRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogs(self, request):
        """本接口(DescribeBinlogs)用于查询云数据库实例的 binlog 文件列表。

        :param request: Request instance for DescribeBinlogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdbProxyInfo(self, request):
        """查询数据库代理详情信息

        :param request: Request instance for DescribeCdbProxyInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbProxyInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbProxyInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdbProxyInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdbProxyInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdbZoneConfig(self, request):
        """本接口(DescribeCdbZoneConfig)用于查询云数据库各地域可售卖的规格配置。

        :param request: Request instance for DescribeCdbZoneConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbZoneConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCdbZoneConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdbZoneConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdbZoneConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloneList(self, request):
        """本接口(DescribeCloneList) 用于查询用户实例的克隆任务列表。

        :param request: Request instance for DescribeCloneList.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCloneListRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCloneListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloneList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloneListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInfo(self, request):
        """本接口(DescribeClusterInfo)用于查询集群版实例信息。

        :param request: Request instance for DescribeClusterInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeClusterInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeClusterInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCpuExpandStrategy(self, request):
        """通过该 API 可以查询实例的 CPU 弹性扩容策略

        :param request: Request instance for DescribeCpuExpandStrategy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeCpuExpandStrategyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeCpuExpandStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCpuExpandStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCpuExpandStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBFeatures(self, request):
        """本接口(DescribeDBFeatures)用于查询云数据库版本属性，包括是否支持数据库加密、数据库审计等功能。

        :param request: Request instance for DescribeDBFeatures.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBFeaturesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBFeaturesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBFeatures", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBFeaturesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBImportRecords(self, request):
        """本接口(DescribeDBImportRecords)用于查询云数据库导入任务操作日志。

        :param request: Request instance for DescribeDBImportRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBImportRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBImportRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBImportRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBImportRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceCharset(self, request):
        """本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。

        :param request: Request instance for DescribeDBInstanceCharset.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceCharsetRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceCharsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceCharset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceCharsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceConfig(self, request):
        """本接口(DescribeDBInstanceConfig)用于云数据库实例的配置信息，包括同步模式，部署模式等。

        :param request: Request instance for DescribeDBInstanceConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceGTID(self, request):
        """本接口(DescribeDBInstanceGTID)用于查询云数据库实例是否开通了 GTID，不支持版本为 5.5 以及以下的实例。

        :param request: Request instance for DescribeDBInstanceGTID.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceGTIDRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceGTID", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceGTIDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceInfo(self, request):
        """查询实例基本信息（实例 ID ，实例名称，是否开通加密 ）

        :param request: Request instance for DescribeDBInstanceInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceLogToCLS(self, request):
        """本接口(DescribeDBInstanceLogToCLS)用于查询实例慢日志、错误日志投递CLS的配置，通过AppId、Region以及实例ID过滤出当前实例日志投递CLS的配置。

        :param request: Request instance for DescribeDBInstanceLogToCLS.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceLogToCLSRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceLogToCLSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceLogToCLS", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceLogToCLSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceRebootTime(self, request):
        """本接口(DescribeDBInstanceRebootTime)用于查询云数据库实例重启预计所需的时间。

        :param request: Request instance for DescribeDBInstanceRebootTime.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceRebootTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceRebootTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目 ID、实例 ID、访问地址、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBPrice(self, request):
        """本接口(DescribeDBPrice)用于查询购买或续费云数据库实例的价格，支持查询按量计费或者包年包月的价格。可传入实例类型、购买时长、购买数量、内存大小、硬盘大小和可用区信息等来查询实例价格。可传入实例名称来查询实例续费价格。

        注意：对某个地域进行询价，请使用对应地域的接入点，接入点信息请参照 <a href="https://cloud.tencent.com/document/api/236/15832">服务地址</a> 文档。例如：对广州地域进行询价，请把请求发到：cdb.ap-guangzhou.tencentcloudapi.com。同理对上海地域询价，把请求发到：cdb.ap-shanghai.tencentcloudapi.com。

        :param request: Request instance for DescribeDBPrice.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBPriceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeDBSwitchRecords(self, request):
        """本接口(DescribeDBSwitchRecords)用于查询云数据库实例切换记录。

        :param request: Request instance for DescribeDBSwitchRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSwitchRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSwitchRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSwitchRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSwitchRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataBackupOverview(self, request):
        """本接口(DescribeDataBackupOverview)用于查询用户在当前地域总的数据备份概览。

        :param request: Request instance for DescribeDataBackupOverview.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDataBackupOverviewRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDataBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """本接口(DescribeDatabases)用于查询云数据库实例的数据库信息，仅支持主实例和灾备实例，不支持只读实例。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultParams(self, request):
        """该接口（DescribeDefaultParams）用于查询默认的可设置参数列表。

        :param request: Request instance for DescribeDefaultParams.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDefaultParamsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDefaultParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeployGroupList(self, request):
        """本接口(DescribeDeployGroupList)用于查询用户的置放群组列表，可以指定置放群组 ID 或置放群组名称。

        :param request: Request instance for DescribeDeployGroupList.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeployGroupListRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeployGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeployGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeployGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDeviceMonitorInfo(self, request):
        """本接口（DescribeDeviceMonitorInfo）用于查询云数据库物理机当天的监控信息，暂只支持内存488G、硬盘6T的实例查询。

        :param request: Request instance for DescribeDeviceMonitorInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDeviceMonitorInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDeviceMonitorInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeErrorLogData(self, request):
        """根据检索条件查询实例错误日志详情。只能查询一个月之内的错误日志。
        使用时需要注意：可能存在单条错误日志太大，导致整个http请求的回包太大，进而引发接口超时。一旦发生超时，建议您缩小查询时的Limit参数值，从而降低包的大小，让接口能够及时返回内容。

        :param request: Request instance for DescribeErrorLogData.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeErrorLogDataRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeErrorLogDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeErrorLogData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeErrorLogDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceAlarmEvents(self, request):
        """查询实例发生的事件信息

        :param request: Request instance for DescribeInstanceAlarmEvents.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceAlarmEventsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAlarmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAlarmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        """该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamRecordsResponse`

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
        """该接口（DescribeInstanceParams）用于查询实例的参数列表。

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamsResponse`

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


    def DescribeLocalBinlogConfig(self, request):
        """该接口用于查询实例本地binlog保留策略。

        :param request: Request instance for DescribeLocalBinlogConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeLocalBinlogConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeLocalBinlogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLocalBinlogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLocalBinlogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplateInfo(self, request):
        """该接口（DescribeParamTemplateInfo）用于查询参数模板详情，全地域公共参数Region均为ap-guangzhou。

        :param request: Request instance for DescribeParamTemplateInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplateInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplateInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplateInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplateInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplates(self, request):
        """该接口（DescribeParamTemplates）查询参数模板列表，全地域公共参数Region均为ap-guangzhou。

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribeProxyCustomConf(self, request):
        """查询代理规格配置

        :param request: Request instance for DescribeProxyCustomConf.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProxyCustomConfRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProxyCustomConfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyCustomConf", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyCustomConfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySupportParam(self, request):
        """查询实例支持代理版本和参数

        :param request: Request instance for DescribeProxySupportParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProxySupportParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProxySupportParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySupportParam", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySupportParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRemoteBackupConfig(self, request):
        """本接口(DescribeRemoteBackupConfig)用于查询数据库异地备份配置信息。

        :param request: Request instance for DescribeRemoteBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRemoteBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRemoteBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRemoteBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRemoteBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoGroups(self, request):
        """本接口(DescribeRoGroups)用于查询云数据库实例的所有的RO组的信息。

        :param request: Request instance for DescribeRoGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRoGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRoGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoMinScale(self, request):
        """本接口(DescribeRoMinScale)用于获取只读实例购买、升级时的最小规格。

        :param request: Request instance for DescribeRoMinScale.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRoMinScaleRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRoMinScaleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoMinScale", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoMinScaleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackRangeTime(self, request):
        """本接口(DescribeRollbackRangeTime)用于查询云数据库实例可回档的时间范围。

        :param request: Request instance for DescribeRollbackRangeTime.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackRangeTimeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackRangeTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackRangeTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackRangeTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTaskDetail(self, request):
        """本接口(DescribeRollbackTaskDetail)用于查询云数据库实例回档任务详情。

        :param request: Request instance for DescribeRollbackTaskDetail.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackTaskDetailRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSSLStatus(self, request):
        """查询 SSL 开通情况。如果已经开通 SSL ，会同步返回证书下载链接。

        :param request: Request instance for DescribeSSLStatus.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSSLStatusRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSSLStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSSLStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSSLStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogData(self, request):
        """条件检索实例的慢日志。只允许查看一个月之内的慢日志。
        使用时需要注意：可能存在单条慢日志太大，导致整个http请求的回包太大，进而引发接口超时。一旦发生超时，建议您缩小查询时的Limit参数值，从而降低包的大小，让接口能够及时返回内容。

        :param request: Request instance for DescribeSlowLogData.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogDataRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogData", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowLogs(self, request):
        """本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。说明：若单次查询数据量过大，则有可能响应超时，建议缩短单次查询时间范围，如一小时，避免导致超时。

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupportedPrivileges(self, request):
        """本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。

        :param request: Request instance for DescribeSupportedPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSupportedPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSupportedPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportedPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportedPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        """本接口(DescribeTables)用于查询云数据库实例的数据库表信息，仅支持主实例和灾备实例，不支持只读实例。

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagsOfInstanceIds(self, request):
        """本接口(DescribeTagsOfInstanceIds)用于获取云数据库实例的标签信息。

        :param request: Request instance for DescribeTagsOfInstanceIds.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagsOfInstanceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsOfInstanceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """本接口(DescribeTasks)用于查询云数据库实例任务列表。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimeWindow(self, request):
        """本接口(DescribeTimeWindow)用于查询云数据库实例的维护时间窗口。

        :param request: Request instance for DescribeTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadedFiles(self, request):
        """本接口(DescribeUploadedFiles)用于查询用户导入的SQL文件列表，全地域公共参数Region均为ap-shanghai。

        :param request: Request instance for DescribeUploadedFiles.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeUploadedFilesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeUploadedFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadedFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadedFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DisassociateSecurityGroupsResponse`

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


    def InitDBInstances(self, request):
        """该接口不再维护，参考CreateDBInstance+API文档，在发货时即可完成初始化。

        本接口(InitDBInstances)用于初始化云数据库实例，包括初始化密码、默认字符集、实例端口号等。该接口已经废弃，在发货接口CreateDBInstance、CreateDBInstanceHour可以直接使用参数Password设置密码，使用参数ParamList设置字符集，使用参数Port设置端口号。

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InitDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpgradeInstances(self, request):
        """本接口(InquiryPriceUpgradeInstances)用于查询云数据库实例升级的价格，支持查询按量计费或者包年包月实例的升级价格，实例类型支持主实例、灾备实例和只读实例。

        :param request: Request instance for InquiryPriceUpgradeInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.InquiryPriceUpgradeInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.InquiryPriceUpgradeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpgradeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpgradeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDBInstance(self, request):
        """本接口(IsolateDBInstance)用于隔离云数据库实例，隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountDescription(self, request):
        """本接口(ModifyAccountDescription)用于修改云数据库账户的备注信息。

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountHost(self, request):
        """本接口(ModifyAccountHost)用于修改云数据库账户的主机。

        :param request: Request instance for ModifyAccountHost.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountHostRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountHostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountHost", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountHostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountMaxUserConnections(self, request):
        """本接口(ModifyAccountMaxUserConnections)用于修改云数据库账户最大可用连接数。

        :param request: Request instance for ModifyAccountMaxUserConnections.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountMaxUserConnectionsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountMaxUserConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountMaxUserConnections", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountMaxUserConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPassword(self, request):
        """本接口(ModifyAccountPassword)用于修改云数据库账户的密码。

        :param request: Request instance for ModifyAccountPassword.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPasswordRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """本接口(ModifyAccountPrivileges)用于修改云数据库的账户的权限信息。

        注意，修改账号权限时，需要传入该账号下的全量权限信息。用户可以先通过 [查询云数据库账户的权限信息
        ](https://cloud.tencent.com/document/api/236/17500) 查询该账号下的全量权限信息，然后进行权限修改。

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditConfig(self, request):
        """本接口(ModifyAuditConfig)用于修改云数据库审计策略的服务配置，包括审计日志保存时长等。

        :param request: Request instance for ModifyAuditConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditRule(self, request):
        """本接口(ModifyAuditRule)用于修改用户的审计规则。

        :param request: Request instance for ModifyAuditRule.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditRuleRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditRuleTemplates(self, request):
        """修改审计规则模板

        :param request: Request instance for ModifyAuditRuleTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAuditService(self, request):
        """本接口(ModifyAuditService)用于修改云数据库审计日志保存时长、审计规则等服务配置

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAutoRenewFlag(self, request):
        """本接口(ModifyAutoRenewFlag)用于修改云数据库实例的自动续费标记。仅支持包年包月的实例设置自动续费标记。

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupConfig(self, request):
        """本接口(ModifyBackupConfig)用于修改数据库备份配置信息。

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupDownloadRestriction(self, request):
        """该接口用于修改用户当前地域的备份文件限制下载来源，可以设置内外网均可下载、仅内网可下载，或内网指定的vpc、ip可以下载。

        :param request: Request instance for ModifyBackupDownloadRestriction.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupEncryptionStatus(self, request):
        """本接口(ModifyBackupEncryptionStatus)用于设置实例备份文件是否加密。

        :param request: Request instance for ModifyBackupEncryptionStatus.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupEncryptionStatusRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupEncryptionStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupEncryptionStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupEncryptionStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdbProxyAddressDesc(self, request):
        """修改代理地址描述信息

        :param request: Request instance for ModifyCdbProxyAddressDesc.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressDescRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressDescResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdbProxyAddressDesc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdbProxyAddressDescResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdbProxyAddressVipAndVPort(self, request):
        """修改数据库代理地址VPC信息

        :param request: Request instance for ModifyCdbProxyAddressVipAndVPort.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressVipAndVPortRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyAddressVipAndVPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdbProxyAddressVipAndVPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdbProxyAddressVipAndVPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdbProxyParam(self, request):
        """配置数据库代理参数

        :param request: Request instance for ModifyCdbProxyParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyCdbProxyParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdbProxyParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdbProxyParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceLogToCLS(self, request):
        """开启/关闭CDB慢日志、错误日志投递CLS

        :param request: Request instance for ModifyDBInstanceLogToCLS.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceLogToCLSRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceLogToCLSResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceLogToCLS", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceLogToCLSResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        """本接口(ModifyDBInstanceName)用于修改云数据库实例的名称。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceProject(self, request):
        """本接口(ModifyDBInstanceProject)用于修改云数据库实例的所属项目。

        :param request: Request instance for ModifyDBInstanceProject.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBInstanceVipVport(self, request):
        """本接口(ModifyDBInstanceVipVport)用于修改云数据库实例的IP和端口号，也可进行基础网络转 VPC 网络和 VPC 网络下的子网变更。

        :param request: Request instance for ModifyDBInstanceVipVport.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceVipVportRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceVipVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceVipVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceVipVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParam(self, request):
        """本接口(ModifyInstanceParam)用于修改云数据库实例的参数。

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancePasswordComplexity(self, request):
        """本接口(ModifyInstancePasswordComplexity)用于修改云数据库实例的密码复杂度。

        :param request: Request instance for ModifyInstancePasswordComplexity.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstancePasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstancePasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancePasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancePasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceTag(self, request):
        """本接口(ModifyInstanceTag)用于对实例标签进行添加、修改或者删除。

        :param request: Request instance for ModifyInstanceTag.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceTagRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceTag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLocalBinlogConfig(self, request):
        """该接口用于修改实例本地binlog保留策略。

        :param request: Request instance for ModifyLocalBinlogConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyLocalBinlogConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyLocalBinlogConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLocalBinlogConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLocalBinlogConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNameOrDescByDpId(self, request):
        """修改置放群组的名称或者描述

        :param request: Request instance for ModifyNameOrDescByDpId.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNameOrDescByDpId", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNameOrDescByDpIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParamTemplate(self, request):
        """该接口（ModifyParamTemplate）用于修改参数模板，全地域公共参数Region均为ap-guangzhou。

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyParamTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyParamTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyParamTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRemoteBackupConfig(self, request):
        """本接口(ModifyRemoteBackupConfig)用于修改数据库异地备份配置信息。

        :param request: Request instance for ModifyRemoteBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyRemoteBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyRemoteBackupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRemoteBackupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRemoteBackupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoGroupInfo(self, request):
        """本接口（ModifyRoGroupInfo）用于更新云数据库只读组的信息。包括设置实例延迟超限剔除策略，设置只读实例读权重，设置复制延迟时间等。

        :param request: Request instance for ModifyRoGroupInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyRoGroupInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyRoGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTimeWindow(self, request):
        """本接口(ModifyTimeWindow)用于更新云数据库实例的维护时间窗口。

        :param request: Request instance for ModifyTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyTimeWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTimeWindow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTimeWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineIsolatedInstances(self, request):
        """本接口(OfflineIsolatedInstances)用于立即下线隔离状态的云数据库实例。进行操作的实例状态必须为隔离状态，即通过 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询到 Status 值为 5 的实例。

        该接口为异步操作，部分资源的回收可能存在延迟。您可以通过使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口，指定实例 InstanceId 和状态 Status 为 [5,6,7] 进行查询，若返回实例为空，则实例资源已全部释放。

        注意，实例下线后，相关资源和数据将无法找回，请谨慎操作。

        :param request: Request instance for OfflineIsolatedInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OfflineIsolatedInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OfflineIsolatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineIsolatedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineIsolatedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        """CDB实例开通审计服务

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenAuditServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenAuditService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenAuditServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBInstanceEncryption(self, request):
        """本接口(OpenDBInstanceEncryption)用于启用实例数据存储加密功能，支持用户指定自定义密钥。

        注意，启用实例数据存储加密之前，需要进行以下操作：

        1、进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作；

        2、开启 [KMS服务](https://console.cloud.tencent.com/kms2)；

        3、对云数据库(MySQL)[授予访问KMS密钥的权限](https://console.cloud.tencent.com/cam/role)，角色名为MySQL_QCSRole，预设策略名为QcloudAccessForMySQLRole；

        该 API 耗时可能到10s，客户端可能超时，如果调用 API 返回 InternalError ，请您调用DescribeDBInstanceInfo 确认后端加密是否开通成功。

        :param request: Request instance for OpenDBInstanceEncryption.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceEncryptionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceEncryptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBInstanceEncryption", params, headers=headers)
            response = json.loads(body)
            model = models.OpenDBInstanceEncryptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBInstanceGTID(self, request):
        """本接口(OpenDBInstanceGTID)用于开启云数据库实例的 GTID，只支持版本为 5.6 以及以上的实例。

        :param request: Request instance for OpenDBInstanceGTID.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceGTIDRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBInstanceGTID", params, headers=headers)
            response = json.loads(body)
            model = models.OpenDBInstanceGTIDResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenSSL(self, request):
        """开启SSL连接功能。

        :param request: Request instance for OpenSSL.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenSSLRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenSSL", params, headers=headers)
            response = json.loads(body)
            model = models.OpenSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWanService(self, request):
        """本接口(OpenWanService)用于开通实例外网访问。

        注意，实例开通外网访问之前，需要先将实例进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作。

        :param request: Request instance for OpenWanService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenWanServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenWanServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenWanService", params, headers=headers)
            response = json.loads(body)
            model = models.OpenWanServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseIsolatedDBInstances(self, request):
        """本接口（ReleaseIsolatedDBInstances）用于恢复已隔离云数据库实例。仅用于按量计费实例的解隔离，包年包月实例的解隔离请使用 RenewDBInstance 。

        :param request: Request instance for ReleaseIsolatedDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ReleaseIsolatedDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ReleaseIsolatedDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIsolatedDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIsolatedDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReloadBalanceProxyNode(self, request):
        """重新负载均衡数据库代理

        :param request: Request instance for ReloadBalanceProxyNode.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ReloadBalanceProxyNodeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ReloadBalanceProxyNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReloadBalanceProxyNode", params, headers=headers)
            response = json.loads(body)
            model = models.ReloadBalanceProxyNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDBInstance(self, request):
        """本接口(RenewDBInstance)用于续费云数据库实例，支持付费模式为包年包月的实例。按量计费实例可通过该接口续费为包年包月的实例。

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRootAccount(self, request):
        """重置实例ROOT账号，初始化账号权限

        :param request: Request instance for ResetRootAccount.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ResetRootAccountRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ResetRootAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRootAccount", params, headers=headers)
            response = json.loads(body)
            model = models.ResetRootAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDBInstances(self, request):
        """本接口(RestartDBInstances)用于重启云数据库实例。

        注意：
        1、本接口只支持主实例进行重启操作；
        2、实例状态必须为正常，并且没有其他异步任务在执行中。

        :param request: Request instance for RestartDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.RestartDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.RestartDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBatchRollback(self, request):
        """该接口（StartBatchRollback）用于批量回档云数据库实例的库表。

        :param request: Request instance for StartBatchRollback.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartBatchRollbackRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartBatchRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBatchRollback", params, headers=headers)
            response = json.loads(body)
            model = models.StartBatchRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCpuExpand(self, request):
        """通过该API，可以开启CPU弹性扩容，包括一次性的手动扩容以及自动弹性扩容。

        :param request: Request instance for StartCpuExpand.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartCpuExpandRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartCpuExpandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCpuExpand", params, headers=headers)
            response = json.loads(body)
            model = models.StartCpuExpandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartReplication(self, request):
        """开启 RO 复制，从主实例同步数据。

        :param request: Request instance for StartReplication.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartReplicationRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartReplication", params, headers=headers)
            response = json.loads(body)
            model = models.StartReplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCpuExpand(self, request):
        """通过该API，可以关闭 CPU 弹性扩容。

        :param request: Request instance for StopCpuExpand.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopCpuExpandRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopCpuExpandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCpuExpand", params, headers=headers)
            response = json.loads(body)
            model = models.StopCpuExpandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDBImportJob(self, request):
        """本接口(StopDBImportJob)用于终止数据导入任务。

        :param request: Request instance for StopDBImportJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopDBImportJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopDBImportJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDBImportJob", params, headers=headers)
            response = json.loads(body)
            model = models.StopDBImportJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopReplication(self, request):
        """停止 RO 复制，中断从主实例同步数据。

        :param request: Request instance for StopReplication.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopReplicationRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopReplicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopReplication", params, headers=headers)
            response = json.loads(body)
            model = models.StopReplicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRollback(self, request):
        """本接口(StopRollback) 用于撤销实例正在进行的回档任务，该接口返回一个异步任务id。 撤销结果可以通过 DescribeAsyncRequestInfo 查询任务的执行情况。

        :param request: Request instance for StopRollback.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopRollbackRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRollback", params, headers=headers)
            response = json.loads(body)
            model = models.StopRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchCDBProxy(self, request):
        """数据库代理配置变更或则升级版本后手动发起立即切换

        :param request: Request instance for SwitchCDBProxy.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchCDBProxyRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchCDBProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchCDBProxy", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchCDBProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDBInstanceMasterSlave(self, request):
        """该接口 (SwitchDBInstanceMasterSlave) 支持用户主动切换实例主从角色。

        :param request: Request instance for SwitchDBInstanceMasterSlave.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchDBInstanceMasterSlaveRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchDBInstanceMasterSlaveResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstanceMasterSlave", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDBInstanceMasterSlaveResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDrInstanceToMaster(self, request):
        """本接口(SwitchDrInstanceToMaster)用于将云数据库灾备实例切换为主实例，注意请求必须发到灾备实例所在的地域。

        :param request: Request instance for SwitchDrInstanceToMaster.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchDrInstanceToMasterRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchDrInstanceToMasterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDrInstanceToMaster", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDrInstanceToMasterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchForUpgrade(self, request):
        """本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程。

        :param request: Request instance for SwitchForUpgrade.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchForUpgradeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchForUpgradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchForUpgrade", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchForUpgradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeCDBProxyVersion(self, request):
        """升级数据库代理版本

        :param request: Request instance for UpgradeCDBProxyVersion.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeCDBProxyVersionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeCDBProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeCDBProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeCDBProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """本接口(UpgradeDBInstance)用于升级或降级云数据库实例的配置，实例类型支持主实例、灾备实例和只读实例。如果进行迁移业务，请一定填写实例规格（CPU、内存），不然系统会默认以最小允许规格传参。

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstanceEngineVersion(self, request):
        """本接口(UpgradeDBInstanceEngineVersion)用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例。

        :param request: Request instance for UpgradeDBInstanceEngineVersion.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceEngineVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceEngineVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VerifyRootAccount(self, request):
        """本接口(VerifyRootAccount)用于校验云数据库实例的 ROOT 账号是否有足够的权限进行授权操作。

        :param request: Request instance for VerifyRootAccount.
        :type request: :class:`tencentcloud.cdb.v20170320.models.VerifyRootAccountRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.VerifyRootAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VerifyRootAccount", params, headers=headers)
            response = json.loads(body)
            model = models.VerifyRootAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))