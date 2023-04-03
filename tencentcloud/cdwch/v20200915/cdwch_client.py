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
from tencentcloud.cdwch.v20200915 import models


class CdwchClient(AbstractClient):
    _apiVersion = '2020-09-15'
    _endpoint = 'cdwch.tencentcloudapi.com'
    _service = 'cdwch'


    def ActionAlterCkUser(self, request):
        """新增和修改用户接口

        :param request: Request instance for ActionAlterCkUser.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ActionAlterCkUserRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ActionAlterCkUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActionAlterCkUser", params, headers=headers)
            response = json.loads(body)
            model = models.ActionAlterCkUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBackUpSchedule(self, request):
        """创建或者修改备份策略

        :param request: Request instance for CreateBackUpSchedule.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.CreateBackUpScheduleRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.CreateBackUpScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackUpSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackUpScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInstanceNew(self, request):
        """创建集群

        :param request: Request instance for CreateInstanceNew.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.CreateInstanceNewRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.CreateInstanceNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstanceNew", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstanceNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackUpSchedule(self, request):
        """查询备份策略信息

        :param request: Request instance for DescribeBackUpSchedule.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeBackUpScheduleRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeBackUpScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackUpSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackUpScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCkSqlApis(self, request):
        """查询集群用户、集群表，数据库等相关信息

        :param request: Request instance for DescribeCkSqlApis.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeCkSqlApisRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeCkSqlApisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCkSqlApis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCkSqlApisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterConfigs(self, request):
        """获取集群的最新的几个配置文件（config.xml、metrika.xml、user.xml）的内容，显示给用户

        :param request: Request instance for DescribeClusterConfigs.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstance(self, request):
        """根据实例ID查询某个实例的具体信息

        :param request: Request instance for DescribeInstance.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceClusters(self, request):
        """集群vcluster列表

        :param request: Request instance for DescribeInstanceClusters.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceClustersRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceKeyValConfigs(self, request):
        """在集群详情页面获取所有参数列表

        :param request: Request instance for DescribeInstanceKeyValConfigs.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceKeyValConfigsRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceKeyValConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceKeyValConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceKeyValConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceShards(self, request):
        """获取实例shard信息列表

        :param request: Request instance for DescribeInstanceShards.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceShardsRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceShardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceShards", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceShardsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceState(self, request):
        """集群详情页中显示集群状态、流程进度等

        :param request: Request instance for DescribeInstanceState.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceStateRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeInstanceStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceState", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSpec(self, request):
        """购买页拉取集群的数据节点和zookeeper节点的规格列表

        :param request: Request instance for DescribeSpec.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DescribeSpecRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DescribeSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DestroyInstance(self, request):
        """销毁集群 open api

        :param request: Request instance for DestroyInstance.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.DestroyInstanceRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.DestroyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyClusterConfigs(self, request):
        """在集群配置页面修改集群配置文件接口，xml模式

        :param request: Request instance for ModifyClusterConfigs.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ModifyClusterConfigsRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ModifyClusterConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstanceKeyValConfigs(self, request):
        """KV模式修改配置接口

        :param request: Request instance for ModifyInstanceKeyValConfigs.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ModifyInstanceKeyValConfigsRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ModifyInstanceKeyValConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceKeyValConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceKeyValConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUserNewPrivilege(self, request):
        """针对ck账号的权限做管控（新版）

        :param request: Request instance for ModifyUserNewPrivilege.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ModifyUserNewPrivilegeRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ModifyUserNewPrivilegeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserNewPrivilege", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserNewPrivilegeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OpenBackUp(self, request):
        """开启或者关闭策略

        :param request: Request instance for OpenBackUp.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.OpenBackUpRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.OpenBackUpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenBackUp", params, headers=headers)
            response = json.loads(body)
            model = models.OpenBackUpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResizeDisk(self, request):
        """扩容磁盘，包含扩容数据节点，zk节点

        :param request: Request instance for ResizeDisk.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ResizeDiskRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ResizeDiskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResizeDisk", params, headers=headers)
            response = json.loads(body)
            model = models.ResizeDiskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScaleOutInstance(self, request):
        """调整clickhouse节点数量

        :param request: Request instance for ScaleOutInstance.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ScaleOutInstanceRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ScaleOutInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleOutInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleOutInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ScaleUpInstance(self, request):
        """垂直扩缩容节点规格，修改节点cvm的规格cpu，内存。 规格变化阶段，服务不可用。

        :param request: Request instance for ScaleUpInstance.
        :type request: :class:`tencentcloud.cdwch.v20200915.models.ScaleUpInstanceRequest`
        :rtype: :class:`tencentcloud.cdwch.v20200915.models.ScaleUpInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ScaleUpInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ScaleUpInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)