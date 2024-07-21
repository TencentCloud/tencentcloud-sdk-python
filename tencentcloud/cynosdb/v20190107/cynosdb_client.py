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
from tencentcloud.cynosdb.v20190107 import models


class CynosdbClient(AbstractClient):
    _apiVersion = '2019-01-07'
    _endpoint = 'cynosdb.tencentcloudapi.com'
    _service = 'cynosdb'


    def ActivateInstance(self, request):
        """本接口(ActivateInstance)用于恢复已隔离的实例访问。

        :param request: Request instance for ActivateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ActivateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddClusterSlaveZone(self, request):
        """开启多可用区部署

        :param request: Request instance for AddClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            model = models.AddClusterSlaveZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddInstances(self, request):
        """本接口（AddInstances）用于集群添加实例

        :param request: Request instance for AddInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AddInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AddInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """安全组批量绑定云资源

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.AssociateSecurityGroupsResponse`

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


    def BindClusterResourcePackages(self, request):
        """为集群绑定资源包

        :param request: Request instance for BindClusterResourcePackages.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.BindClusterResourcePackagesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.BindClusterResourcePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindClusterResourcePackages", params, headers=headers)
            response = json.loads(body)
            model = models.BindClusterResourcePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseAuditService(self, request):
        """TDSQL-C for MySQL实例关闭审计服务

        :param request: Request instance for CloseAuditService.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseAuditServiceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseAuditServiceResponse`

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


    def CloseClusterPasswordComplexity(self, request):
        """本接口（CloseClusterPasswordComplexity）用于关闭集群密码复杂度

        :param request: Request instance for CloseClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.CloseClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseProxy(self, request):
        """关闭数据库代理

        :param request: Request instance for CloseProxy.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseProxyRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CloseProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseWan(self, request):
        """本接口（CloseWan）用于关闭外网

        :param request: Request instance for CloseWan.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CloseWanRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CloseWanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseWan", params, headers=headers)
            response = json.loads(body)
            model = models.CloseWanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyClusterPasswordComplexity(self, request):
        """本接口（CopyClusterPasswordComplexity）用于复制集群密码复杂度

        :param request: Request instance for CopyClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CopyClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CopyClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.CopyClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccounts(self, request):
        """创建用户账号

        :param request: Request instance for CreateAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAccountsResponse`

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
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAuditLogFileRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAuditLogFileResponse`

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


    def CreateAuditRuleTemplate(self, request):
        """创建审计规则模板

        :param request: Request instance for CreateAuditRuleTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateAuditRuleTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateAuditRuleTemplateResponse`

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
        """为集群创建手动备份

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateBackupResponse`

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


    def CreateCLSDelivery(self, request):
        """创建日志投递

        :param request: Request instance for CreateCLSDelivery.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateCLSDeliveryRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateCLSDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCLSDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCLSDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterDatabase(self, request):
        """创建数据库

        :param request: Request instance for CreateClusterDatabase.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateClusterDatabaseRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateClusterDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusters(self, request):
        """购买新集群

        :param request: Request instance for CreateClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusters", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateParamTemplate(self, request):
        """本接口（CreateParamTemplate）用于创建参数模板

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateParamTemplateResponse`

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


    def CreateProxy(self, request):
        """创建数据库代理

        :param request: Request instance for CreateProxy.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateProxyEndPoint(self, request):
        """创建数据库代理连接点

        :param request: Request instance for CreateProxyEndPoint.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyEndPointRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateProxyEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateProxyEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateProxyEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourcePackage(self, request):
        """新购资源包

        :param request: Request instance for CreateResourcePackage.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.CreateResourcePackageRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.CreateResourcePackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourcePackage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourcePackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccounts(self, request):
        """删除用户账号

        :param request: Request instance for DeleteAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAccountsResponse`

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
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAuditLogFileRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAuditLogFileResponse`

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


    def DeleteAuditRuleTemplates(self, request):
        """删除审计规则模板

        :param request: Request instance for DeleteAuditRuleTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteAuditRuleTemplatesResponse`

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
        """为集群删除手动备份，无法删除自动备份

        :param request: Request instance for DeleteBackup.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteBackupRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteBackupResponse`

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


    def DeleteCLSDelivery(self, request):
        """删除日志投递

        :param request: Request instance for DeleteCLSDelivery.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteCLSDeliveryRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteCLSDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCLSDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCLSDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterDatabase(self, request):
        """删除数据库

        :param request: Request instance for DeleteClusterDatabase.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteClusterDatabaseRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteClusterDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParamTemplate(self, request):
        """本接口（DeleteParamTemplate）用于删除用户创建的参数模板。

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DeleteParamTemplateResponse`

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


    def DescribeAccountAllGrantPrivileges(self, request):
        """查询账号所有可授予权限

        :param request: Request instance for DescribeAccountAllGrantPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountAllGrantPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountAllGrantPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountAllGrantPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountAllGrantPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivileges(self, request):
        """查询账号已有权限

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountPrivilegesResponse`

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
        """本接口(DescribeAccounts)用于查询数据库账号列表

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAccountsResponse`

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


    def DescribeAuditInstanceList(self, request):
        """获取审计实例列表

        :param request: Request instance for DescribeAuditInstanceList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditInstanceListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditInstanceListResponse`

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
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditLogFilesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditLogFilesResponse`

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
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditLogsResponse`

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


    def DescribeAuditRuleTemplates(self, request):
        """查询审计规则模板信息

        :param request: Request instance for DescribeAuditRuleTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleTemplatesResponse`

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


    def DescribeAuditRuleWithInstanceIds(self, request):
        """获取实例的审计规则

        :param request: Request instance for DescribeAuditRuleWithInstanceIds.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleWithInstanceIdsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeAuditRuleWithInstanceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAuditRuleWithInstanceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAuditRuleWithInstanceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupConfig(self, request):
        """获取指定集群的备份配置信息，包括全量备份时间段，备份文件保留时间

        :param request: Request instance for DescribeBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupConfigResponse`

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


    def DescribeBackupDownloadUrl(self, request):
        """此接口（DescribeBackupDownloadUrl）用于查询集群备份文件下载地址。

        :param request: Request instance for DescribeBackupDownloadUrl.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupList(self, request):
        """查询备份文件列表

        :param request: Request instance for DescribeBackupList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBackupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogDownloadUrl(self, request):
        """此接口（DescribeBinlogDownloadUrl）用于查询Binlog的下载地址。

        :param request: Request instance for DescribeBinlogDownloadUrl.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogDownloadUrlRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogSaveDays(self, request):
        """此接口（DescribeBinlogSaveDays）用于查询集群的Binlog保留天数。

        :param request: Request instance for DescribeBinlogSaveDays.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogSaveDaysRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogSaveDaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBinlogSaveDays", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBinlogSaveDaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBinlogs(self, request):
        """此接口（DescribeBinlogs）用来查询集群Binlog日志列表。

        :param request: Request instance for DescribeBinlogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeBinlogsResponse`

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


    def DescribeChangedParamsAfterUpgrade(self, request):
        """本接口（DescribeChangedParamsAfterUpgrade）用于查询升降配运行参数对比

        :param request: Request instance for DescribeChangedParamsAfterUpgrade.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeChangedParamsAfterUpgradeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeChangedParamsAfterUpgradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChangedParamsAfterUpgrade", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChangedParamsAfterUpgradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDatabases(self, request):
        """获取集群数据库列表

        :param request: Request instance for DescribeClusterDatabases.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDatabasesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetail(self, request):
        """该接口（DescribeClusterDetail）显示集群详情

        :param request: Request instance for DescribeClusterDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterDetailDatabases(self, request):
        """查询数据库列表

        :param request: Request instance for DescribeClusterDetailDatabases.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailDatabasesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterDetailDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterDetailDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterDetailDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstanceGroups(self, request):
        """本接口（DescribeClusterInstanceGrps）用于查询实例组信息。

        :param request: Request instance for DescribeClusterInstanceGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstanceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstanceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterInstanceGrps(self, request):
        """本接口（DescribeClusterInstanceGrps）用于查询实例组信息。 该接口已废弃，推荐使用DescribeClusterInstanceGroups

        :param request: Request instance for DescribeClusterInstanceGrps.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterInstanceGrpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterInstanceGrps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterInstanceGrpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterParamLogs(self, request):
        """本接口（DescribeClusterParamLogs）查询参数修改记录

        :param request: Request instance for DescribeClusterParamLogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterParamLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterParamLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterParams(self, request):
        """本接口（DescribeClusterParams）用于查询集群参数

        :param request: Request instance for DescribeClusterParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterPasswordComplexity(self, request):
        """本接口（DescribeClusterPasswordComplexity）用于查看集群密码复杂度详情

        :param request: Request instance for DescribeClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusters(self, request):
        """查询集群列表

        :param request: Request instance for DescribeClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """查询实例安全组信息

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeFlow(self, request):
        """本接口（DescribeFlow）用于查询任务流信息

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceCLSLogDelivery(self, request):
        """查询实例日志投递信息

        :param request: Request instance for DescribeInstanceCLSLogDelivery.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceCLSLogDeliveryRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceCLSLogDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceCLSLogDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceCLSLogDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceDetail(self, request):
        """本接口(DescribeInstanceDetail)用于查询实例详情。

        :param request: Request instance for DescribeInstanceDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceErrorLogs(self, request):
        """查询实例错误日志列表

        :param request: Request instance for DescribeInstanceErrorLogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceErrorLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceErrorLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceErrorLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceErrorLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        """该接口(DescribeInstanceParams)查询实例参数列表

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceParamsResponse`

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


    def DescribeInstanceSlowQueries(self, request):
        """此接口（DescribeInstanceSlowQueries）用于查询实例慢日志详情。

        :param request: Request instance for DescribeInstanceSlowQueries.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSlowQueriesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSlowQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSlowQueries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSlowQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceSpecs(self, request):
        """本接口（DescribeInstanceSpecs）用于查询购买页可购买的实例规格

        :param request: Request instance for DescribeInstanceSpecs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """本接口(DescribeInstances)用于查询实例列表。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeInstancesResponse`

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


    def DescribeMaintainPeriod(self, request):
        """查询实例维护时间窗

        :param request: Request instance for DescribeMaintainPeriod.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeMaintainPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintainPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintainPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplateDetail(self, request):
        """本接口（DescribeParamTemplateDetail）用于查询用户参数模板详情

        :param request: Request instance for DescribeParamTemplateDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplateDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplateDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamTemplateDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamTemplateDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamTemplates(self, request):
        """查询用户指定产品下的所有参数模板信息

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeParamTemplatesResponse`

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
        """查询项目安全组信息

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribeProxies(self, request):
        """查询数据库代理列表

        :param request: Request instance for DescribeProxies.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxiesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxyNodes(self, request):
        """本接口（DescribeProxyNodes）用于查询代理节点列表。

        :param request: Request instance for DescribeProxyNodes.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxyNodesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxyNodesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxyNodes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxyNodesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProxySpecs(self, request):
        """查询数据库代理规格

        :param request: Request instance for DescribeProxySpecs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxySpecsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeProxySpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProxySpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProxySpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePackageDetail(self, request):
        """查询资源包使用详情

        :param request: Request instance for DescribeResourcePackageDetail.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageDetailRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePackageDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePackageDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePackageList(self, request):
        """查询资源包列表

        :param request: Request instance for DescribeResourcePackageList.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageListRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePackageList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePackageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcePackageSaleSpec(self, request):
        """查询资源包规格

        :param request: Request instance for DescribeResourcePackageSaleSpec.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageSaleSpecRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcePackageSaleSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcePackageSaleSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcePackageSaleSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcesByDealName(self, request):
        """查询订单关联实例

        :param request: Request instance for DescribeResourcesByDealName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeResourcesByDealNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByDealName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesByDealNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTimeRange(self, request):
        """查询回档时间范围

        :param request: Request instance for DescribeRollbackTimeRange.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTimeRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTimeValidity(self, request):
        """历史废弃接口，从云API下线

        指定时间和集群查询是否可回滚

        :param request: Request instance for DescribeRollbackTimeValidity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeRollbackTimeValidityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTimeValidity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTimeValidityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupportProxyVersion(self, request):
        """查询支持的数据库代理版本

        :param request: Request instance for DescribeSupportProxyVersion.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeSupportProxyVersionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeSupportProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasks(self, request):
        """查询任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeTasksResponse`

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


    def DescribeZones(self, request):
        """本接口(DescribeZones)用于查询可售卖地域可用区信息。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """安全组批量解绑云资源

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.DisassociateSecurityGroupsResponse`

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


    def ExportInstanceErrorLogs(self, request):
        """此接口（ExportInstanceErrorLogs）用于导出实例错误日志。

        :param request: Request instance for ExportInstanceErrorLogs.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceErrorLogsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceErrorLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportInstanceErrorLogs", params, headers=headers)
            response = json.loads(body)
            model = models.ExportInstanceErrorLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportInstanceSlowQueries(self, request):
        """此接口（ExportInstanceSlowQueries）用于导出实例慢日志。

        :param request: Request instance for ExportInstanceSlowQueries.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceSlowQueriesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ExportInstanceSlowQueriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportInstanceSlowQueries", params, headers=headers)
            response = json.loads(body)
            model = models.ExportInstanceSlowQueriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExportResourcePackageDeductDetails(self, request):
        """资源包使用明细导出

        :param request: Request instance for ExportResourcePackageDeductDetails.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ExportResourcePackageDeductDetailsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ExportResourcePackageDeductDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExportResourcePackageDeductDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ExportResourcePackageDeductDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantAccountPrivileges(self, request):
        """批量授权账号权限

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.GrantAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreate(self, request):
        """查询新购集群价格

        :param request: Request instance for InquirePriceCreate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceCreateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceCreateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreate", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRenew(self, request):
        """查询续费集群价格

        :param request: Request instance for InquirePriceRenew.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceRenewRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.InquirePriceRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRenew", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRenewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateCluster(self, request):
        """隔离集群

        :param request: Request instance for IsolateCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateCluster", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateInstance(self, request):
        """本接口(IsolateInstance)用于隔离实例。

        :param request: Request instance for IsolateInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.IsolateInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountDescription(self, request):
        """本接口(ModifyAccountDescription)用于修改数据库账号描述信息。

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountDescriptionResponse`

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
        """修改账号主机

        :param request: Request instance for ModifyAccountHost.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountHostRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountHostResponse`

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


    def ModifyAccountParams(self, request):
        """修改账号配置

        :param request: Request instance for ModifyAccountParams.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountParamsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountParams", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """修改账号库表权限

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAccountPrivilegesResponse`

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


    def ModifyAuditRuleTemplates(self, request):
        """修改审计规则模板

        :param request: Request instance for ModifyAuditRuleTemplates.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditRuleTemplatesResponse`

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
        """本接口(ModifyAuditService)用于修改云数据库审计日志保存时长、审计规则等服务配置。

        :param request: Request instance for ModifyAuditService.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditServiceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyAuditServiceResponse`

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


    def ModifyBackupConfig(self, request):
        """修改指定集群的备份配置

        :param request: Request instance for ModifyBackupConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupConfigResponse`

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


    def ModifyBackupName(self, request):
        """此接口（ModifyBackupName）用于修改备份文件备注名。

        :param request: Request instance for ModifyBackupName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBackupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBinlogSaveDays(self, request):
        """此接口（ModifyBinlogSaveDays）用于修改集群Binlog保留天数。

        :param request: Request instance for ModifyBinlogSaveDays.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBinlogSaveDaysRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyBinlogSaveDaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBinlogSaveDays", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBinlogSaveDaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterDatabase(self, request):
        """修改数据库

        :param request: Request instance for ModifyClusterDatabase.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterDatabaseRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterName(self, request):
        """修改集群名称

        :param request: Request instance for ModifyClusterName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterParam(self, request):
        """修改集群参数

        :param request: Request instance for ModifyClusterParam.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterPasswordComplexity(self, request):
        """本接口（ModifyClusterPasswordComplexity）用于修改/开启集群密码复杂度

        :param request: Request instance for ModifyClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterSlaveZone(self, request):
        """变更备可用区

        :param request: Request instance for ModifyClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterSlaveZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyClusterStorage(self, request):
        """调整包年包月存储容量

        :param request: Request instance for ModifyClusterStorage.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterStorageRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyClusterStorageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterStorage", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterStorageResponse()
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
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyInstanceName(self, request):
        """本接口(ModifyInstanceName)用于修改实例名称。

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParam(self, request):
        """本接口（ModifyInstanceParam）用于修改实例参数。

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceParamResponse`

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


    def ModifyInstanceUpgradeLimitDays(self, request):
        """修改实例小版本升级限制时间

        :param request: Request instance for ModifyInstanceUpgradeLimitDays.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceUpgradeLimitDaysRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyInstanceUpgradeLimitDaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceUpgradeLimitDays", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceUpgradeLimitDaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaintainPeriodConfig(self, request):
        """修改维护时间配置

        :param request: Request instance for ModifyMaintainPeriodConfig.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyMaintainPeriodConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintainPeriodConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintainPeriodConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParamTemplate(self, request):
        """本接口（ModifyParamTemplate）用于修改用户参数模板。

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyParamTemplateResponse`

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


    def ModifyProxyDesc(self, request):
        """修改数据库代理描述

        :param request: Request instance for ModifyProxyDesc.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyDescRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyDescResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxyDesc", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxyDescResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyProxyRwSplit(self, request):
        """配置数据库代理读写分离

        :param request: Request instance for ModifyProxyRwSplit.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyRwSplitRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyProxyRwSplitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyProxyRwSplit", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyProxyRwSplitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePackageClusters(self, request):
        """给资源包绑定集群

        :param request: Request instance for ModifyResourcePackageClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePackageClusters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePackageClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePackageName(self, request):
        """修改资源包名称

        :param request: Request instance for ModifyResourcePackageName.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageNameRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackageNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePackageName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePackageNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcePackagesDeductionPriority(self, request):
        """修改已绑定资源包抵扣优先级

        :param request: Request instance for ModifyResourcePackagesDeductionPriority.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackagesDeductionPriorityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyResourcePackagesDeductionPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcePackagesDeductionPriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcePackagesDeductionPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVipVport(self, request):
        """修改实例组ip，端口

        :param request: Request instance for ModifyVipVport.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ModifyVipVportRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ModifyVipVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVipVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVipVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineCluster(self, request):
        """销毁集群

        :param request: Request instance for OfflineCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineCluster", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OfflineInstance(self, request):
        """销毁实例

        :param request: Request instance for OfflineInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OfflineInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OfflineInstance", params, headers=headers)
            response = json.loads(body)
            model = models.OfflineInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenAuditService(self, request):
        """TDSQL-C for MySQL实例开通审计服务

        :param request: Request instance for OpenAuditService.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenAuditServiceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenAuditServiceResponse`

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


    def OpenClusterPasswordComplexity(self, request):
        """本接口（OpenClusterPasswordComplexity）用于开启自定义密码复杂度功能

        :param request: Request instance for OpenClusterPasswordComplexity.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterPasswordComplexityRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterPasswordComplexityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenClusterPasswordComplexity", params, headers=headers)
            response = json.loads(body)
            model = models.OpenClusterPasswordComplexityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenClusterReadOnlyInstanceGroupAccess(self, request):
        """开启只读实例组接入

        :param request: Request instance for OpenClusterReadOnlyInstanceGroupAccess.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterReadOnlyInstanceGroupAccessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenClusterReadOnlyInstanceGroupAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenClusterReadOnlyInstanceGroupAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenClusterReadOnlyInstanceGroupAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenReadOnlyInstanceExclusiveAccess(self, request):
        """开通只读实例独有访问接入组

        :param request: Request instance for OpenReadOnlyInstanceExclusiveAccess.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenReadOnlyInstanceExclusiveAccessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenReadOnlyInstanceExclusiveAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenReadOnlyInstanceExclusiveAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenReadOnlyInstanceExclusiveAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenWan(self, request):
        """本接口（OpenWan）用于开通外网

        :param request: Request instance for OpenWan.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.OpenWanRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.OpenWanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenWan", params, headers=headers)
            response = json.loads(body)
            model = models.OpenWanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PauseServerless(self, request):
        """暂停serverless集群

        :param request: Request instance for PauseServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.PauseServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseServerless", params, headers=headers)
            response = json.loads(body)
            model = models.PauseServerlessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefundResourcePackage(self, request):
        """退款资源包

        :param request: Request instance for RefundResourcePackage.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RefundResourcePackageRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RefundResourcePackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefundResourcePackage", params, headers=headers)
            response = json.loads(body)
            model = models.RefundResourcePackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReloadBalanceProxyNode(self, request):
        """负载均衡数据库代理

        :param request: Request instance for ReloadBalanceProxyNode.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ReloadBalanceProxyNodeRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ReloadBalanceProxyNodeResponse`

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


    def RemoveClusterSlaveZone(self, request):
        """关闭多可用区部署

        :param request: Request instance for RemoveClusterSlaveZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RemoveClusterSlaveZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RemoveClusterSlaveZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveClusterSlaveZone", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveClusterSlaveZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewClusters(self, request):
        """续费集群

        :param request: Request instance for RenewClusters.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RenewClustersRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RenewClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewClusters", params, headers=headers)
            response = json.loads(body)
            model = models.RenewClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        """本接口(ResetAccountPassword)用于修改数据库账号密码

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ResetAccountPasswordResponse`

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
        """重启实例

        :param request: Request instance for RestartInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RestartInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RestartInstanceResponse`

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


    def ResumeServerless(self, request):
        """恢复serverless集群

        :param request: Request instance for ResumeServerless.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.ResumeServerlessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeServerless", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeServerlessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeAccountPrivileges(self, request):
        """批量回收账号权限

        :param request: Request instance for RevokeAccountPrivileges.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RevokeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RevokeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollBackCluster(self, request):
        """本接口（RollBackCluster）用于集群回档

        :param request: Request instance for RollBackCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RollBackClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RollBackClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollBackCluster", params, headers=headers)
            response = json.loads(body)
            model = models.RollBackClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackToNewCluster(self, request):
        """回档到新集群

        :param request: Request instance for RollbackToNewCluster.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.RollbackToNewClusterRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.RollbackToNewClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackToNewCluster", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackToNewClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClusterDatabases(self, request):
        """本接口(SearchClusterDatabases)搜索集群数据库列表

        :param request: Request instance for SearchClusterDatabases.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterDatabasesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClusterDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClusterDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchClusterTables(self, request):
        """本接口(SearchClusterTables)搜索集群数据表列表

        :param request: Request instance for SearchClusterTables.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterTablesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SearchClusterTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchClusterTables", params, headers=headers)
            response = json.loads(body)
            model = models.SearchClusterTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetRenewFlag(self, request):
        """SetRenewFlag设置实例的自动续费功能

        :param request: Request instance for SetRenewFlag.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SetRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.SetRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartCLSDelivery(self, request):
        """开启日志投递

        :param request: Request instance for StartCLSDelivery.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.StartCLSDeliveryRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.StartCLSDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartCLSDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.StartCLSDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopCLSDelivery(self, request):
        """停止日志投递

        :param request: Request instance for StopCLSDelivery.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.StopCLSDeliveryRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.StopCLSDeliveryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopCLSDelivery", params, headers=headers)
            response = json.loads(body)
            model = models.StopCLSDeliveryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchClusterVpc(self, request):
        """更换集群vpc

        :param request: Request instance for SwitchClusterVpc.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterVpcRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchClusterVpc", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchClusterVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchClusterZone(self, request):
        """主备可用区切换

        :param request: Request instance for SwitchClusterZone.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterZoneRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchClusterZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchClusterZone", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchClusterZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchProxyVpc(self, request):
        """本接口(SwitchProxyVpc)更换数据库代理vpc

        :param request: Request instance for SwitchProxyVpc.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.SwitchProxyVpcRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.SwitchProxyVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchProxyVpc", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchProxyVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindClusterResourcePackages(self, request):
        """cynos解绑资源包

        :param request: Request instance for UnbindClusterResourcePackages.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UnbindClusterResourcePackagesRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UnbindClusterResourcePackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindClusterResourcePackages", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindClusterResourcePackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeClusterVersion(self, request):
        """更新内核小版本

        :param request: Request instance for UpgradeClusterVersion.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeClusterVersionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeClusterVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeClusterVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeClusterVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeInstance(self, request):
        """实例变配

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeInstanceResponse`

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


    def UpgradeProxy(self, request):
        """升级数据库代理配置

        :param request: Request instance for UpgradeProxy.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeProxy", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeProxyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeProxyVersion(self, request):
        """升级数据库代理版本

        :param request: Request instance for UpgradeProxyVersion.
        :type request: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyVersionRequest`
        :rtype: :class:`tencentcloud.cynosdb.v20190107.models.UpgradeProxyVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeProxyVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeProxyVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))