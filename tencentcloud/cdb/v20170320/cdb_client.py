# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


    def AssociateSecurityGroups(self, request):
        """本接口(AssociateSecurityGroups)用于安全组批量绑定实例。

        :param request: 调用AssociateSecurityGroups所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloseWanService(self, request):
        """本接口(CloseWanService)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问。

        :param request: 调用CloseWanService所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBackup(self, request):
        """本接口(CreateBackup)用于创建数据库备份。

        :param request: 调用CreateBackup所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDBImportJob(self, request):
        """本接口(CreateDBImportJob)用于创建云数据库数据导入任务。

        :param request: 调用CreateDBImportJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDBInstance(self, request):
        """本接口(CreateDBInstance)用于创建包年包月的云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、MySQL 版本号、购买时长和数量等信息创建云数据库实例。

        您还可以使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询该实例的详细信息。

        1. 首先请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口查询可创建的实例规格信息，然后请使用[查询价格（包年包月）](https://cloud.tencent.com/document/api/236/1332)接口查询可创建实例的售卖价格；

        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；

        3. 支持创建 MySQL5.5 、 MySQL5.6 、 MySQL5.7 版本；

        4. 支持创建主实例、只读实例、灾备实例；

        :param request: 调用CreateDBInstance所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDBInstanceHour(self, request):
        """本接口(CreateDBInstanceHour)用于创建按量计费的实例，可通过传入实例规格、MySQL 版本号和数量等信息创建云数据库实例，支持主实例、灾备实例和只读实例的创建。

        您还可以使用[查询实例列表](https://cloud.tencent.com/document/api/236/15872)接口查询该实例的详细信息。

        1. 首先请使用[获取云数据库可售卖规格](https://cloud.tencent.com/document/api/236/17229)接口查询可创建的实例规格信息，然后请使用[查询价格（按量计费）](https://cloud.tencent.com/document/api/253/5176)接口查询可创建实例的售卖价格；
        2. 单次创建实例最大支持 100 个，实例时长最大支持 36 个月；
        3. 支持创建 MySQL5.5、MySQL5.6和MySQL5.7 版本；
        4. 支持创建主实例、灾备实例和只读实例；

        :param request: 调用CreateDBInstanceHour所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteBackup(self, request):
        """本接口(DeleteBackup)用于删除数据库备份。

        :param request: 调用DeleteBackup所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupConfig(self, request):
        """本接口(DescribeBackupConfig)用于查询数据库备份配置信息。

        :param request: 调用DescribeBackupConfig所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupDatabases(self, request):
        """本接口(DescribeBackupDatabases)用于查询备份数据库列表。

        :param request: 调用DescribeBackupDatabases所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupDownloadDbTableCode(self, request):
        """本接口(DescribeBackupDownloadDbTableCode)用于查询备份数据分库分表下载位点。

        :param request: 调用DescribeBackupDownloadDbTableCode所需参数的结构体。
        :type request: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDownloadDbTableCodeRequest`
        :rtype: :class:`tencentcloud.cdb.v20170320.models.DescribeBackupDownloadDbTableCodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupDownloadDbTableCode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupDownloadDbTableCodeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupTables(self, request):
        """本接口(DescribeBackupTables)用于查询指定的数据库的备份数据表名。

        :param request: 调用DescribeBackupTables所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackups(self, request):
        """本接口(DescribeBackups)用于查询云数据库实例的备份数据。

        :param request: 调用DescribeBackups所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBinlogs(self, request):
        """本接口(DescribeBinlogs)用于查询云数据库实例的二进制数据。

        :param request: 调用DescribeBinlogs所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBImportRecords(self, request):
        """本接口(DescribeDBImportRecords)用于查询云数据库导入任务操作日志。

        :param request: 调用DescribeDBImportRecords所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstanceCharset(self, request):
        """本接口(DescribeDBInstanceCharset)用于查询云数据库实例的字符集，获取字符集的名称。

        :param request: 调用DescribeDBInstanceCharset所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstanceGTID(self, request):
        """本接口(DescribeDBInstanceGTID)用于查询云数据库实例是否开通了GTID，不支持版本为5.5以及以下的实例。

        :param request: 调用DescribeDBInstanceGTID所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstanceRebootTime(self, request):
        """本接口(DescribeDBInstanceRebootTime)用于查询云数据库实例重启预计所需的时间。

        :param request: 调用DescribeDBInstanceRebootTime所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstances(self, request):
        """本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、访问地址、实例状态等来筛选实例。

        1. 不指定任何过滤条件, 则默认返回20条实例记录，单次请求最多支持返回100条实例记录；
        2. 支持查询主实例、灾备实例和只读实例信息列表。

        :param request: 调用DescribeDBInstances所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSecurityGroups(self, request):
        """本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: 调用DescribeDBSecurityGroups所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBZoneConfig(self, request):
        """本接口(DescribeDBZoneConfig)用于查询可创建的云数据库各地域可售卖的规格配置。

        :param request: 调用DescribeDBZoneConfig所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjectSecurityGroups(self, request):
        """本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。

        :param request: 调用DescribeProjectSecurityGroups所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSlowLogs(self, request):
        """本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。

        :param request: 调用DescribeSlowLogs所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """本接口(DescribeTasks)用于查询云数据库实例任务列表。

        :param request: 调用DescribeTasks所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: 调用DisassociateSecurityGroups所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InitDBInstances(self, request):
        """本接口(InitDBInstances)用于初始化云数据库实例，包括初始化密码、默认字符集、实例端口号等

        :param request: 调用InitDBInstances所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def IsolateDBInstance(self, request):
        """本接口(IsolateDBInstance)用于销毁云数据库实例，销毁之后不能通过IP和端口访问数据库，按量计费实例销毁后直接下线。

        本接口不支持包年包月实例；

        :param request: 调用IsolateDBInstance所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBackupConfig(self, request):
        """本接口(ModifyBackupConfig)用于修改数据库备份配置信息。

        :param request: 调用ModifyBackupConfig所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceName(self, request):
        """本接口(ModifyDBInstanceName)用于修改云数据库实例的名称。

        :param request: 调用ModifyDBInstanceName所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceProject(self, request):
        """本接口(ModifyDBInstanceProject)用于修改云数据库实例的所属项目。

        :param request: 调用ModifyDBInstanceProject所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: 调用ModifyDBInstanceSecurityGroups所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceVipVport(self, request):
        """本接口(ModifyDBInstanceVipVport)用于修改云数据库实例的IP和端口号，也可进行基础网络转VPC网络和VPC网络下的子网变更。

        :param request: 调用ModifyDBInstanceVipVport所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceParam(self, request):
        """本接口(ModifyInstanceParam)用于修改云数据库实例的参数。

        :param request: 调用ModifyInstanceParam所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenWanService(self, request):
        """本接口(OpenWanService)用于开通实例外网访问

        :param request: 调用OpenWanService所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopDBImportJob(self, request):
        """本接口(StopDBImportJob)用于终止数据导入任务。

        :param request: 调用StopDBImportJob所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchForUpgrade(self, request):
        """本接口(SwitchForUpgrade)用于切换访问新实例，针对主升级中的实例处于待切换状态时，用户可主动发起该流程

        :param request: 调用SwitchForUpgrade所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeDBInstance(self, request):
        """本接口(UpgradeDBInstance)用于升级云数据库实例，实例类型支持主实例、灾备实例和只读实例

        :param request: 调用UpgradeDBInstance所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeDBInstanceEngineVersion(self, request):
        """本接口(UpgradeDBInstanceEngineVersion)用于升级云数据库实例版本，实例类型支持主实例、灾备实例和只读实例。

        :param request: 调用UpgradeDBInstanceEngineVersion所需参数的结构体。
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)