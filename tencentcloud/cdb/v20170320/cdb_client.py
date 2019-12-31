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
from tencentcloud.cdb.v20170320 import models


class CdbClient(AbstractClient):
    _apiVersion = '2017-03-20'
    _endpoint = 'cdb.tencentcloudapi.com'


    def AddTimeWindow(self, request):
        """本接口(AddTimeWindow)用于添加云数据库实例的维护时间窗口，以指定实例在哪些时间段可以自动执行切换访问操作。

        :param request: Request instance for AddTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AddTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AddTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTimeWindowResponse()
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


    def AssociateSecurityGroups(self, request):
        """本接口(AssociateSecurityGroups)用于安全组批量绑定实例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
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


    def CloseWanService(self, request):
        """本接口(CloseWanService)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问。

        :param request: Request instance for CloseWanService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CloseWanServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CloseWanServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseWanService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseWanServiceResponse()
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


    def CreateAccounts(self, request):
        """本接口(CreateAccounts)用于创建云数据库的账户，需要指定新的账户名和域名，以及所对应的密码，同时可以设置账号的备注信息。

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountsResponse()
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


    def CreateBackup(self, request):
        """本接口(CreateBackup)用于创建数据库备份。

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
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


    def CreateDBImportJob(self, request):
        """本接口(CreateDBImportJob)用于创建云数据库数据导入任务。

        注意，用户进行数据导入任务的文件，必须提前上传到腾讯云。用户须在控制台进行文件导入。

        :param request: Request instance for CreateDBImportJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBImportJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBImportJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBImportJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBImportJobResponse()
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


    def CreateDBInstance(self, request):
        """本接口(CreateDBInstance)用于创建包年包月的云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、MySQL 版本号、购买时长和数量等信息创建云数据库实例。

        该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为1，且 TaskStatus 为0，表示实例已经发货成功。

        1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL 5.5 、 MySQL 5.6 、 MySQL 5.7 版本；
        4. 支持创建主实例、只读实例、灾备实例；
        5. 当入参指定 Port，ParamList 或 Password 时，该实例会进行初始化操作；

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceResponse()
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


    def CreateDBInstanceHour(self, request):
        """本接口(CreateDBInstanceHour)用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。

        该接口为异步接口，您还可以使用 [查询实例列表](https://cloud.tencent.com/document/api/236/15872) 接口查询该实例的详细信息。当该实例的 Status 为 1，且 TaskStatus 为 0，表示实例已经发货成功。

        1. 首先请使用 [获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229) 接口查询可创建的实例规格信息，然后请使用 [查询数据库价格](https://cloud.tencent.com/document/api/236/18566) 接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL 5.5、MySQL 5.6 和 MySQL 5.7 版本；
        4. 支持创建主实例、灾备实例和只读实例；
        5. 当入参指定 Port，ParamList 或 Password 时，该实例会进行初始化操作；

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceHourResponse()
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


    def CreateDeployGroup(self, request):
        """本接口(CreateDeployGroup)用于创建放置实例的置放群组

        :param request: Request instance for CreateDeployGroup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateDeployGroupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateDeployGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDeployGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDeployGroupResponse()
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


    def CreateParamTemplate(self, request):
        """该接口（CreateParamTemplate）用于创建参数模板。

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.CreateParamTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateParamTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateParamTemplateResponse()
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


    def DeleteAccounts(self, request):
        """本接口(DeleteAccounts)用于删除云数据库的账户。

        :param request: Request instance for DeleteAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountsResponse()
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


    def DeleteBackup(self, request):
        """本接口(DeleteBackup)用于删除数据库备份。

        :param request: Request instance for DeleteBackup.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteBackupRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBackupResponse()
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


    def DeleteDeployGroups(self, request):
        """根据置放群组ID删除置放群组（置放群组中有资源存在时不能删除该置放群组）

        :param request: Request instance for DeleteDeployGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteDeployGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteDeployGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDeployGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeployGroupsResponse()
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


    def DeleteParamTemplate(self, request):
        """该接口（DeleteParamTemplate）用于删除参数模板。

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteParamTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteParamTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteParamTemplateResponse()
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


    def DeleteTimeWindow(self, request):
        """本接口(DeleteTimeWindow)用于删除云数据库实例的维护时间窗口。删除实例维护时间窗口之后，默认的维护时间窗为 03:00-04:00，即当选择在维护时间窗口内切换访问新实例时，默认会在 03:00-04:00 点进行切换访问新实例。

        :param request: Request instance for DeleteTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DeleteTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DeleteTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTimeWindowResponse()
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


    def DescribeAccountPrivileges(self, request):
        """本接口(DescribeAccountPrivileges)用于查询云数据库账户支持的权限信息。

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
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


    def DescribeAccounts(self, request):
        """本接口(DescribeAccounts)用于查询云数据库的所有账户信息。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
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


    def DescribeAsyncRequestInfo(self, request):
        """本接口(DescribeAsyncRequestInfo)用于查询云数据库实例异步任务的执行结果。

        :param request: Request instance for DescribeAsyncRequestInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeAsyncRequestInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeAsyncRequestInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAsyncRequestInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAsyncRequestInfoResponse()
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


    def DescribeBackupConfig(self, request):
        """本接口(DescribeBackupConfig)用于查询数据库备份配置信息。

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupConfigResponse()
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


    def DescribeBackupDatabases(self, request):
        """本接口(DescribeBackupDatabases)用于查询备份文件包含的库 (已废弃)。
        旧版本支持全量备份后，用户如果分库表下载逻辑备份文件，需要用到此接口。
        新版本支持(CreateBackup)创建逻辑备份的时候，直接发起指定库表备份，用户直接下载该备份文件即可。

        :param request: Request instance for DescribeBackupDatabases.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDatabasesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupDatabasesResponse()
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


    def DescribeBackupTables(self, request):
        """本接口(DescribeBackupTables)用于查询指定的数据库的备份数据表名 (已废弃)。
        旧版本支持全量备份后，用户如果分库表下载逻辑备份文件，需要用到此接口。
        新版本支持(CreateBackup)创建逻辑备份的时候，直接发起指定库表备份，用户直接下载该备份文件即可。

        :param request: Request instance for DescribeBackupTables.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupTablesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupTablesResponse()
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


    def DescribeBackups(self, request):
        """本接口(DescribeBackups)用于查询云数据库实例的备份数据。

        :param request: Request instance for DescribeBackups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupsResponse()
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


    def DescribeBinlogs(self, request):
        """本接口(DescribeBinlogs)用于查询云数据库实例的二进制数据。

        :param request: Request instance for DescribeBinlogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBinlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBinlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBinlogsResponse()
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


    def DescribeDBImportRecords(self, request):
        """本接口(DescribeDBImportRecords)用于查询云数据库导入任务操作日志。

        :param request: Request instance for DescribeDBImportRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBImportRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBImportRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBImportRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBImportRecordsResponse()
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


    def DescribeDBInstanceCharset(self, request):
        """本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。

        :param request: Request instance for DescribeDBInstanceCharset.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceCharsetRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceCharsetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceCharset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceCharsetResponse()
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


    def DescribeDBInstanceConfig(self, request):
        """本接口(DescribeDBInstanceConfig)用于云数据库实例的配置信息，包括同步模式，部署模式等。

        :param request: Request instance for DescribeDBInstanceConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceConfigResponse()
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


    def DescribeDBInstanceGTID(self, request):
        """本接口(DescribeDBInstanceGTID)用于查询云数据库实例是否开通了 GTID，不支持版本为 5.5 以及以下的实例。

        :param request: Request instance for DescribeDBInstanceGTID.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceGTIDRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceGTID", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceGTIDResponse()
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


    def DescribeDBInstanceRebootTime(self, request):
        """本接口(DescribeDBInstanceRebootTime)用于查询云数据库实例重启预计所需的时间。

        :param request: Request instance for DescribeDBInstanceRebootTime.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstanceRebootTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceRebootTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceRebootTimeResponse()
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


    def DescribeDBInstances(self, request):
        """本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目 ID、实例 ID、访问地址、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
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


    def DescribeDBPrice(self, request):
        """本接口(DescribeDBPrice)用于查询云数据库实例的价格，支持查询按量计费或者包年包月的价格。可传入实例类型、购买时长、购买数量、内存大小、硬盘大小和可用区信息等来查询实例价格。

        注意：对某个地域进行询价，请使用对应地域的接入点，接入点信息请参照 <a href="https://cloud.tencent.com/document/api/236/15832">服务地址</a> 文档。例如：对广州地域进行询价，请把请求发到：cdb.ap-guangzhou.tencentcloudapi.com。同理对上海地域询价，把请求发到：cdb.ap-shanghai.tencentcloudapi.com。

        :param request: Request instance for DescribeDBPrice.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBPriceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPriceResponse()
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


    def DescribeDBSecurityGroups(self, request):
        """本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
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


    def DescribeDBSwitchRecords(self, request):
        """本接口(DescribeDBSwitchRecords)用于查询云数据库实例切换记录。

        :param request: Request instance for DescribeDBSwitchRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSwitchRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBSwitchRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSwitchRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSwitchRecordsResponse()
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


    def DescribeDBZoneConfig(self, request):
        """本接口(DescribeDBZoneConfig)用于查询可创建的云数据库各地域可售卖的规格配置。

        :param request: Request instance for DescribeDBZoneConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDBZoneConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDBZoneConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBZoneConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBZoneConfigResponse()
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


    def DescribeDatabases(self, request):
        """本接口(DescribeDatabases)用于查询云数据库实例的数据库信息。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
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


    def DescribeDefaultParams(self, request):
        """该接口（DescribeDefaultParams）用于查询默认的可设置参数列表。

        :param request: Request instance for DescribeDefaultParams.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDefaultParamsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDefaultParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDefaultParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultParamsResponse()
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


    def DescribeDeployGroupList(self, request):
        """本接口(DescribeDeployGroupList)用于查询用户的置放群组列表，可以指定置放群组 ID 或置放群组名称。

        :param request: Request instance for DescribeDeployGroupList.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeployGroupListRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeployGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeployGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeployGroupListResponse()
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


    def DescribeDeviceMonitorInfo(self, request):
        """本接口（DescribeDeviceMonitorInfo）用于查询云数据库物理机当天的监控信息，暂只支持内存488G、硬盘6T的实例查询。

        :param request: Request instance for DescribeDeviceMonitorInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeDeviceMonitorInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDeviceMonitorInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDeviceMonitorInfoResponse()
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


    def DescribeInstanceParamRecords(self, request):
        """该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParamRecords", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamRecordsResponse()
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


    def DescribeInstanceParams(self, request):
        """该接口（DescribeInstanceParams）用于查询实例的参数列表。

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceParamsResponse()
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


    def DescribeParamTemplateInfo(self, request):
        """该接口（DescribeParamTemplateInfo）用于查询参数模板详情。

        :param request: Request instance for DescribeParamTemplateInfo.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplateInfoRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplateInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeParamTemplateInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeParamTemplateInfoResponse()
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


    def DescribeParamTemplates(self, request):
        """该接口（DescribeParamTemplates）查询参数模板列表。

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeParamTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeParamTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeParamTemplatesResponse()
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


    def DescribeProjectSecurityGroups(self, request):
        """本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
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


    def DescribeRollbackRangeTime(self, request):
        """本接口(DescribeRollbackRangeTime)用于查询云数据库实例可回档的时间范围。

        :param request: Request instance for DescribeRollbackRangeTime.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackRangeTimeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeRollbackRangeTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRollbackRangeTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackRangeTimeResponse()
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


    def DescribeSlowLogs(self, request):
        """本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogsResponse()
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


    def DescribeSupportedPrivileges(self, request):
        """本接口(DescribeSupportedPrivileges)用于查询云数据库的支持的权限信息，包括全局权限，数据库权限，表权限以及列权限。

        :param request: Request instance for DescribeSupportedPrivileges.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeSupportedPrivilegesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeSupportedPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSupportedPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSupportedPrivilegesResponse()
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


    def DescribeTables(self, request):
        """本接口(DescribeTables)用于查询云数据库实例的数据库表信息。

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTablesResponse()
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


    def DescribeTagsOfInstanceIds(self, request):
        """本接口(DescribeTagsOfInstanceIds)用于获取云数据库实例的标签信息。

        :param request: Request instance for DescribeTagsOfInstanceIds.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTagsOfInstanceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagsOfInstanceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsOfInstanceIdsResponse()
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


    def DescribeTasks(self, request):
        """本接口(DescribeTasks)用于查询云数据库实例任务列表。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def DescribeTimeWindow(self, request):
        """本接口(DescribeTimeWindow)用于查询云数据库实例的维护时间窗口。

        :param request: Request instance for DescribeTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTimeWindowResponse()
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


    def DescribeUploadedFiles(self, request):
        """本接口(DescribeUploadedFiles)用于查询用户导入的SQL文件列表。

        :param request: Request instance for DescribeUploadedFiles.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeUploadedFilesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeUploadedFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUploadedFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUploadedFilesResponse()
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


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
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


    def InitDBInstances(self, request):
        """本接口(InitDBInstances)用于初始化云数据库实例，包括初始化密码、默认字符集、实例端口号等

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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


    def InquiryPriceUpgradeInstances(self, request):
        """本接口(InquiryPriceUpgradeInstances)用于查询云数据库实例升级的价格，支持查询按量计费或者包年包月实例的升级价格，实例类型支持主实例、灾备实例和只读实例。

        :param request: Request instance for InquiryPriceUpgradeInstances.
        :type request: :class:`tencentcloud.cdb.v20170320.models.InquiryPriceUpgradeInstancesRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.InquiryPriceUpgradeInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeInstancesResponse()
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


    def IsolateDBInstance(self, request):
        """本接口(IsolateDBInstance)用于隔离云数据库实例，隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDBInstanceResponse()
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


    def ModifyAccountDescription(self, request):
        """本接口(ModifyAccountDescription)用于修改云数据库账户的备注信息。

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
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


    def ModifyAccountPassword(self, request):
        """本接口(ModifyAccountPassword)用于修改云数据库账户的密码。

        :param request: Request instance for ModifyAccountPassword.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPasswordRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountPasswordResponse()
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
            body = self.call("ModifyAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountPrivilegesResponse()
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


    def ModifyAutoRenewFlag(self, request):
        """本接口(ModifyAutoRenewFlag)用于修改云数据库实例的自动续费标记。仅支持包年包月的实例设置自动续费标记。

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoRenewFlagResponse()
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


    def ModifyBackupConfig(self, request):
        """本接口(ModifyBackupConfig)用于修改数据库备份配置信息。

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupConfigResponse()
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


    def ModifyDBInstanceName(self, request):
        """本接口(ModifyDBInstanceName)用于修改云数据库实例的名称。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
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


    def ModifyDBInstanceProject(self, request):
        """本接口(ModifyDBInstanceProject)用于修改云数据库实例的所属项目。

        :param request: Request instance for ModifyDBInstanceProject.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceProjectResponse()
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


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
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


    def ModifyDBInstanceVipVport(self, request):
        """本接口(ModifyDBInstanceVipVport)用于修改云数据库实例的IP和端口号，也可进行基础网络转 VPC 网络和 VPC 网络下的子网变更。

        :param request: Request instance for ModifyDBInstanceVipVport.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceVipVportRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyDBInstanceVipVportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceVipVport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceVipVportResponse()
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


    def ModifyInstanceParam(self, request):
        """本接口(ModifyInstanceParam)用于修改云数据库实例的参数。

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceParamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceParam", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceParamResponse()
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


    def ModifyInstanceTag(self, request):
        """本接口(ModifyInstanceTag)用于对实例标签进行添加、修改或者删除。

        :param request: Request instance for ModifyInstanceTag.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceTagRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyInstanceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceTagResponse()
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


    def ModifyNameOrDescByDpId(self, request):
        """修改置放群组的名称或者描述

        :param request: Request instance for ModifyNameOrDescByDpId.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyNameOrDescByDpIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNameOrDescByDpId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNameOrDescByDpIdResponse()
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


    def ModifyParamTemplate(self, request):
        """该接口（ModifyParamTemplate）用于修改参数模板。

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyParamTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyParamTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyParamTemplateResponse()
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


    def ModifyTimeWindow(self, request):
        """本接口(ModifyTimeWindow)用于更新云数据库实例的维护时间窗口。

        :param request: Request instance for ModifyTimeWindow.
        :type request: :class:`tencentcloud.cdb.v20170320.models.ModifyTimeWindowRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.ModifyTimeWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTimeWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTimeWindowResponse()
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
            body = self.call("OfflineIsolatedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OfflineIsolatedInstancesResponse()
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


    def OpenDBInstanceGTID(self, request):
        """本接口(OpenDBInstanceGTID)用于开启云数据库实例的 GTID，只支持版本为 5.6 以及以上的实例。

        :param request: Request instance for OpenDBInstanceGTID.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceGTIDRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenDBInstanceGTIDResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBInstanceGTID", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBInstanceGTIDResponse()
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


    def OpenWanService(self, request):
        """本接口(OpenWanService)用于开通实例外网访问。

        注意，实例开通外网访问之前，需要先将实例进行 [实例初始化](https://cloud.tencent.com/document/api/236/15873) 操作。

        :param request: Request instance for OpenWanService.
        :type request: :class:`tencentcloud.cdb.v20170320.models.OpenWanServiceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.OpenWanServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenWanService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenWanServiceResponse()
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


    def RenewDBInstance(self, request):
        """本接口(RenewDBInstance)用于续费云数据库实例，仅支持付费模式为包年包月的实例。按量计费实例不需要续费。

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstanceResponse()
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
            body = self.call("RestartDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstancesResponse()
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


    def StartBatchRollback(self, request):
        """该接口（StartBatchRollback）用于批量回档云数据库实例的库表。

        :param request: Request instance for StartBatchRollback.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StartBatchRollbackRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StartBatchRollbackResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartBatchRollback", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartBatchRollbackResponse()
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


    def StopDBImportJob(self, request):
        """本接口(StopDBImportJob)用于终止数据导入任务。

        :param request: Request instance for StopDBImportJob.
        :type request: :class:`tencentcloud.cdb.v20170320.models.StopDBImportJobRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.StopDBImportJobResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopDBImportJob", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopDBImportJobResponse()
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


    def SwitchForUpgrade(self, request):
        """本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程。

        :param request: Request instance for SwitchForUpgrade.
        :type request: :class:`tencentcloud.cdb.v20170320.models.SwitchForUpgradeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.SwitchForUpgradeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchForUpgrade", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchForUpgradeResponse()
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


    def UpgradeDBInstance(self, request):
        """本接口(UpgradeDBInstance)用于升级或降级云数据库实例的配置，实例类型支持主实例、灾备实例和只读实例。

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
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


    def UpgradeDBInstanceEngineVersion(self, request):
        """本接口(UpgradeDBInstanceEngineVersion)用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例。

        :param request: Request instance for UpgradeDBInstanceEngineVersion.
        :type request: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.UpgradeDBInstanceEngineVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstanceEngineVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceEngineVersionResponse()
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


    def VerifyRootAccount(self, request):
        """本接口(VerifyRootAccount)用于校验云数据库实例的 ROOT 账号是否有足够的权限进行授权操作。

        :param request: Request instance for VerifyRootAccount.
        :type request: :class:`tencentcloud.cdb.v20170320.models.VerifyRootAccountRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.VerifyRootAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VerifyRootAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VerifyRootAccountResponse()
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