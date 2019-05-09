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
from tencentcloud.tcb.v20180608 import models


class TcbClient(AbstractClient):
    _apiVersion = '2018-06-08'
    _endpoint = 'tcb.tencentcloudapi.com'


    def DescribeDatabaseACL(self, request):
        """获取数据库权限

        :param request: 调用DescribeDatabaseACL所需参数的结构体。
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseACLResponse()
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


    def DescribeEnvs(self, request):
        """获取环境列表，含环境下的各个资源信息。尤其是各资源的唯一标识，是请求各资源的关键参数

        :param request: 调用DescribeEnvs所需参数的结构体。
        :type request: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.DescribeEnvsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEnvs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEnvsResponse()
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


    def ModifyDatabaseACL(self, request):
        """修改数据库权限

        :param request: 调用ModifyDatabaseACL所需参数的结构体。
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyDatabaseACLResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDatabaseACL", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDatabaseACLResponse()
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


    def ModifyEnv(self, request):
        """更新环境信息

        :param request: 调用ModifyEnv所需参数的结构体。
        :type request: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvRequest`
        :rtype: :class:`tencentcloud.tcb.v20180608.models.ModifyEnvResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyEnv", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEnvResponse()
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