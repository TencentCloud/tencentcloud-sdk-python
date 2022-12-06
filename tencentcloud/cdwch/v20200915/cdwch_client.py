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
            if "Error" not in response["Response"]:
                model = models.ActionAlterCkUserResponse()
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
            if "Error" not in response["Response"]:
                model = models.CreateBackUpScheduleResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeCkSqlApisResponse()
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
            if "Error" not in response["Response"]:
                model = models.DescribeSpecResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyClusterConfigsResponse()
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
            if "Error" not in response["Response"]:
                model = models.ModifyUserNewPrivilegeResponse()
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
            if "Error" not in response["Response"]:
                model = models.OpenBackUpResponse()
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