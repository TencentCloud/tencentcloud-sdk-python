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
from tencentcloud.redis.v20180412 import models


class RedisClient(AbstractClient):
    _apiVersion = '2018-04-12'
    _endpoint = 'redis.tencentcloudapi.com'
    _service = 'redis'


    def AddReplicationInstance(self, request):
        """添加复制组成员

        :param request: Request instance for AddReplicationInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.AddReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.AddReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddReplicationInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddReplicationInstanceResponse()
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


    def ApplyParamsTemplate(self, request):
        """应用参数模板到实例

        :param request: Request instance for ApplyParamsTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.ApplyParamsTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ApplyParamsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ApplyParamsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ApplyParamsTemplateResponse()
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
        """本接口 (AssociateSecurityGroups) 用于安全组批量绑定多个指定实例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.redis.v20180412.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.AssociateSecurityGroupsResponse`

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


    def ChangeReplicaToMaster(self, request):
        """该接口仅支持多AZ实例副本组提主和单AZ副本提主

        :param request: Request instance for ChangeReplicaToMaster.
        :type request: :class:`tencentcloud.redis.v20180412.models.ChangeReplicaToMasterRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ChangeReplicaToMasterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ChangeReplicaToMaster", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChangeReplicaToMasterResponse()
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


    def CleanUpInstance(self, request):
        """回收站实例立即下线

        :param request: Request instance for CleanUpInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.CleanUpInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CleanUpInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CleanUpInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CleanUpInstanceResponse()
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


    def ClearInstance(self, request):
        """清空Redis实例的实例数据。

        :param request: Request instance for ClearInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ClearInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ClearInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ClearInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ClearInstanceResponse()
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


    def CreateInstanceAccount(self, request):
        """创建实例子账号

        :param request: Request instance for CreateInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstanceAccountResponse()
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


    def CreateInstances(self, request):
        """本接口(CreateInstances)用于创建redis实例。

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstancesResponse()
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
        """创建参数模板。

        :param request: Request instance for CreateParamTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateParamTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateParamTemplateResponse`

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


    def CreateReplicationGroup(self, request):
        """创建复制组

        :param request: Request instance for CreateReplicationGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.CreateReplicationGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.CreateReplicationGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReplicationGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReplicationGroupResponse()
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


    def DeleteInstanceAccount(self, request):
        """删除实例子账号

        :param request: Request instance for DeleteInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteInstanceAccountResponse()
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
        """删除参数模板

        :param request: Request instance for DeleteParamTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteParamTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteParamTemplateResponse`

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


    def DeleteReplicationInstance(self, request):
        """移除复制组成员

        :param request: Request instance for DeleteReplicationInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DeleteReplicationInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DeleteReplicationInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReplicationInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReplicationInstanceResponse()
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


    def DescribeAutoBackupConfig(self, request):
        """获取备份配置

        :param request: Request instance for DescribeAutoBackupConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAutoBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAutoBackupConfigResponse()
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


    def DescribeBackupUrl(self, request):
        """查询备份Rdb下载地址(接口灰度中，需要加白名单使用)

        :param request: Request instance for DescribeBackupUrl.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeBackupUrlRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeBackupUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupUrlResponse()
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


    def DescribeCommonDBInstances(self, request):
        """查询Redis实例列表信息。该接口已废弃。

        :param request: Request instance for DescribeCommonDBInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeCommonDBInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeCommonDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCommonDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCommonDBInstancesResponse()
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
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeInstanceAccount(self, request):
        """查看实例子账号信息

        :param request: Request instance for DescribeInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceAccountResponse()
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


    def DescribeInstanceBackups(self, request):
        """查询 CRS 实例备份列表

        :param request: Request instance for DescribeInstanceBackups.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceBackupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceBackupsResponse()
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


    def DescribeInstanceDTSInfo(self, request):
        """查询实例DTS信息

        :param request: Request instance for DescribeInstanceDTSInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDTSInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceDTSInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDTSInfoResponse()
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


    def DescribeInstanceDealDetail(self, request):
        """查询订单信息

        :param request: Request instance for DescribeInstanceDealDetail.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDealDetailRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceDealDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceDealDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceDealDetailResponse()
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


    def DescribeInstanceMonitorBigKey(self, request):
        """查询实例大Key

        :param request: Request instance for DescribeInstanceMonitorBigKey.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeyResponse()
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


    def DescribeInstanceMonitorBigKeySizeDist(self, request):
        """查询实例大Key大小分布

        :param request: Request instance for DescribeInstanceMonitorBigKeySizeDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeySizeDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKeySizeDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeySizeDistResponse()
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


    def DescribeInstanceMonitorBigKeyTypeDist(self, request):
        """查询实例大Key类型分布

        :param request: Request instance for DescribeInstanceMonitorBigKeyTypeDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorBigKeyTypeDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorBigKeyTypeDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorBigKeyTypeDistResponse()
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


    def DescribeInstanceMonitorHotKey(self, request):
        """查询实例热Key

        :param request: Request instance for DescribeInstanceMonitorHotKey.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorHotKeyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorHotKey", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorHotKeyResponse()
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


    def DescribeInstanceMonitorSIP(self, request):
        """查询实例访问来源信息

        :param request: Request instance for DescribeInstanceMonitorSIP.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorSIPRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorSIPResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorSIP", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorSIPResponse()
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


    def DescribeInstanceMonitorTookDist(self, request):
        """查询实例访问的耗时分布

        :param request: Request instance for DescribeInstanceMonitorTookDist.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTookDistResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTookDist", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTookDistResponse()
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


    def DescribeInstanceMonitorTopNCmd(self, request):
        """查询实例访问命令

        :param request: Request instance for DescribeInstanceMonitorTopNCmd.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTopNCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTopNCmdResponse()
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


    def DescribeInstanceMonitorTopNCmdTook(self, request):
        """查询实例CPU耗时

        :param request: Request instance for DescribeInstanceMonitorTopNCmdTook.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceMonitorTopNCmdTookResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceMonitorTopNCmdTook", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceMonitorTopNCmdTookResponse()
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


    def DescribeInstanceNodeInfo(self, request):
        """查询实例节点信息

        :param request: Request instance for DescribeInstanceNodeInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceNodeInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceNodeInfoResponse()
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
        """查询参数修改历史列表

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamRecordsResponse`

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
        """查询实例参数列表

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceParamsResponse`

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


    def DescribeInstanceSecurityGroup(self, request):
        """查询实例安全组信息

        :param request: Request instance for DescribeInstanceSecurityGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSecurityGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceSecurityGroupResponse()
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


    def DescribeInstanceShards(self, request):
        """获取集群版实例分片信息

        :param request: Request instance for DescribeInstanceShards.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceShardsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceShardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceShards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceShardsResponse()
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


    def DescribeInstanceZoneInfo(self, request):
        """查询Redis节点详细信息

        :param request: Request instance for DescribeInstanceZoneInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceZoneInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstanceZoneInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceZoneInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceZoneInfoResponse()
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
        """查询Redis实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeInstancesResponse`

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


    def DescribeMaintenanceWindow(self, request):
        """查询实例维护时间窗，在实例需要进行版本升级或者架构升级的时候，会在维护时间窗时间内进行切换

        :param request: Request instance for DescribeMaintenanceWindow.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMaintenanceWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaintenanceWindowResponse()
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
        """查询参数模板详情。

        :param request: Request instance for DescribeParamTemplateInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplateInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplateInfoResponse`

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
        """查询参数模板列表

        :param request: Request instance for DescribeParamTemplates.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplatesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeParamTemplatesResponse`

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


    def DescribeProductInfo(self, request):
        """本接口查询指定可用区和实例类型下 Redis 的售卖规格， 如果用户不在购买白名单中，将不能查询该可用区或该类型的售卖规格详情。申请购买某地域白名单可以提交工单

        :param request: Request instance for DescribeProductInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProductInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProductInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductInfoResponse()
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


    def DescribeProjectSecurityGroup(self, request):
        """查询项目安全组信息

        :param request: Request instance for DescribeProjectSecurityGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupResponse()
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
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribeProxySlowLog(self, request):
        """本接口（DescribeProxySlowLog）用于查询代理慢查询。

        :param request: Request instance for DescribeProxySlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeProxySlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeProxySlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxySlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxySlowLogResponse()
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


    def DescribeReplicationGroup(self, request):
        """查询复制组

        :param request: Request instance for DescribeReplicationGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeReplicationGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeReplicationGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReplicationGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReplicationGroupResponse()
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


    def DescribeSlowLog(self, request):
        """查询实例慢查询记录

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeSlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogResponse()
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


    def DescribeTaskInfo(self, request):
        """用于查询任务结果

        :param request: Request instance for DescribeTaskInfo.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskInfoResponse()
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


    def DescribeTaskList(self, request):
        """查询任务列表信息

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskListResponse()
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


    def DescribeTendisSlowLog(self, request):
        """查询Tendis慢查询

        :param request: Request instance for DescribeTendisSlowLog.
        :type request: :class:`tencentcloud.redis.v20180412.models.DescribeTendisSlowLogRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DescribeTendisSlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTendisSlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTendisSlowLogResponse()
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


    def DestroyPostpaidInstance(self, request):
        """按量计费实例销毁

        :param request: Request instance for DestroyPostpaidInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DestroyPostpaidInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DestroyPostpaidInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyPostpaidInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPostpaidInstanceResponse()
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


    def DestroyPrepaidInstance(self, request):
        """包年包月实例退还

        :param request: Request instance for DestroyPrepaidInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.DestroyPrepaidInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DestroyPrepaidInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyPrepaidInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyPrepaidInstanceResponse()
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


    def DisableReplicaReadonly(self, request):
        """禁用读写分离

        :param request: Request instance for DisableReplicaReadonly.
        :type request: :class:`tencentcloud.redis.v20180412.models.DisableReplicaReadonlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DisableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableReplicaReadonly", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableReplicaReadonlyResponse()
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
        :type request: :class:`tencentcloud.redis.v20180412.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.DisassociateSecurityGroupsResponse`

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


    def EnableReplicaReadonly(self, request):
        """启用读写分离

        :param request: Request instance for EnableReplicaReadonly.
        :type request: :class:`tencentcloud.redis.v20180412.models.EnableReplicaReadonlyRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.EnableReplicaReadonlyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableReplicaReadonly", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableReplicaReadonlyResponse()
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
        """查询新购实例价格

        :param request: Request instance for InquiryPriceCreateInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.InquiryPriceCreateInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.InquiryPriceCreateInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateInstance", params)
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
        """查询实例续费价格（包年包月）

        :param request: Request instance for InquiryPriceRenewInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.InquiryPriceRenewInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.InquiryPriceRenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewInstance", params)
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


    def InquiryPriceUpgradeInstance(self, request):
        """查询实例扩容价格

        :param request: Request instance for InquiryPriceUpgradeInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.InquiryPriceUpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.InquiryPriceUpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeInstanceResponse()
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


    def KillMasterGroup(self, request):
        """模拟故障

        :param request: Request instance for KillMasterGroup.
        :type request: :class:`tencentcloud.redis.v20180412.models.KillMasterGroupRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.KillMasterGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("KillMasterGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.KillMasterGroupResponse()
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


    def ManualBackupInstance(self, request):
        """手动备份Redis实例

        :param request: Request instance for ManualBackupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ManualBackupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualBackupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualBackupInstanceResponse()
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


    def ModfiyInstancePassword(self, request):
        """修改redis密码

        :param request: Request instance for ModfiyInstancePassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModfiyInstancePasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModfiyInstancePasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModfiyInstancePassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModfiyInstancePasswordResponse()
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


    def ModifyAutoBackupConfig(self, request):
        """设置自动备份配置

        :param request: Request instance for ModifyAutoBackupConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyAutoBackupConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyAutoBackupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAutoBackupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAutoBackupConfigResponse()
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


    def ModifyConnectionConfig(self, request):
        """修改实例的连接配置，包括带宽和最大连接数。

        :param request: Request instance for ModifyConnectionConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyConnectionConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyConnectionConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyConnectionConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyConnectionConfigResponse()
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
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyInstance(self, request):
        """修改实例相关信息

        :param request: Request instance for ModifyInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceResponse()
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


    def ModifyInstanceAccount(self, request):
        """修改实例子账号

        :param request: Request instance for ModifyInstanceAccount.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAccountRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceAccountResponse()
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


    def ModifyInstanceParams(self, request):
        """本接口(ModifyInstanceParams)用于修改实例参数。

        :param request: Request instance for ModifyInstanceParams.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceParamsRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstanceParams", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstanceParamsResponse()
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


    def ModifyMaintenanceWindow(self, request):
        """修改实例维护时间窗时间，需要进行版本升级或者架构升级的实例，会在维护时间窗内进行时间切换。注意：已经发起版本升级或者架构升级的实例，无法修改维护时间窗。

        :param request: Request instance for ModifyMaintenanceWindow.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMaintenanceWindow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMaintenanceWindowResponse()
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


    def ModifyNetworkConfig(self, request):
        """修改实例网络配置

        :param request: Request instance for ModifyNetworkConfig.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyNetworkConfigRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyNetworkConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkConfigResponse()
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
        """修改参数模板

        :param request: Request instance for ModifyParamTemplate.
        :type request: :class:`tencentcloud.redis.v20180412.models.ModifyParamTemplateRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ModifyParamTemplateResponse`

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


    def RenewInstance(self, request):
        """续费实例

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstanceResponse()
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


    def ResetPassword(self, request):
        """重置密码

        :param request: Request instance for ResetPassword.
        :type request: :class:`tencentcloud.redis.v20180412.models.ResetPasswordRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.ResetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetPasswordResponse()
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


    def RestoreInstance(self, request):
        """恢复 CRS 实例

        :param request: Request instance for RestoreInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreInstanceResponse()
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


    def StartupInstance(self, request):
        """实例解隔离

        :param request: Request instance for StartupInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.StartupInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.StartupInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartupInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartupInstanceResponse()
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


    def SwitchInstanceVip(self, request):
        """在通过DTS支持跨可用区灾备的场景中，通过该接口交换实例VIP完成实例灾备切换。交换VIP后目标实例可写，源和目标实例VIP互换，同时源与目标实例间DTS同步任务断开

        :param request: Request instance for SwitchInstanceVip.
        :type request: :class:`tencentcloud.redis.v20180412.models.SwitchInstanceVipRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.SwitchInstanceVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwitchInstanceVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwitchInstanceVipResponse()
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
        """升级实例

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceResponse`

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


    def UpgradeInstanceVersion(self, request):
        """将原本实例升级到高版本实例，或者将主从版实例升级到集群版实例

        :param request: Request instance for UpgradeInstanceVersion.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceVersionRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeInstanceVersionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeInstanceVersion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeInstanceVersionResponse()
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


    def UpgradeVersionToMultiAvailabilityZones(self, request):
        """升级实例支持多AZ

        :param request: Request instance for UpgradeVersionToMultiAvailabilityZones.
        :type request: :class:`tencentcloud.redis.v20180412.models.UpgradeVersionToMultiAvailabilityZonesRequest`
        :rtype: :class:`tencentcloud.redis.v20180412.models.UpgradeVersionToMultiAvailabilityZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeVersionToMultiAvailabilityZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeVersionToMultiAvailabilityZonesResponse()
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