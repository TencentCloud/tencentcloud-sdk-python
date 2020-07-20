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
from tencentcloud.habo.v20181203 import models


class HaboClient(AbstractClient):
    _apiVersion = '2018-12-03'
    _endpoint = 'habo.tencentcloudapi.com'


    def DescribeStatus(self, request):
        """查询指定md5样本是否分析完成，并获取分析日志下载地址。

        :param request: Request instance for DescribeStatus.
        :type request: :class:`tencentcloud.habo.v20181203.models.DescribeStatusRequest`
        :rtype: :class:`tencentcloud.habo.v20181203.models.DescribeStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStatusResponse()
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


    def StartAnalyse(self, request):
        """上传样本到哈勃进行分析，异步生成分析日志。

        :param request: Request instance for StartAnalyse.
        :type request: :class:`tencentcloud.habo.v20181203.models.StartAnalyseRequest`
        :rtype: :class:`tencentcloud.habo.v20181203.models.StartAnalyseResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartAnalyse", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartAnalyseResponse()
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