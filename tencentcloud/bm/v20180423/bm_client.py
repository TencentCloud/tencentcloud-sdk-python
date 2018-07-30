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
from tencentcloud.bm.v20180423 import models


class BmClient(AbstractClient):
    _apiVersion = '2018-04-23'
    _endpoint = 'bm.tencentcloudapi.com'


    def DescribeRepairTaskConstant(self, request):
        """维修任务配置获取

        :param request: 调用DescribeRepairTaskConstant所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeRepairTaskConstantRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeRepairTaskConstantResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRepairTaskConstant", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRepairTaskConstantResponse()
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


    def DescribeTaskInfo(self, request):
        """获取用户维修任务列表及详细信息<br>
        <br>
        TaskStatus（任务状态ID）与状态中文名的对应关系如下：<br>
        1：未授权<br>
        2：处理中<br>
        3：待确认<br>
        4：未授权-暂不处理<br>
        5：已恢复<br>
        6：待确认-未恢复<br>

        :param request: 调用DescribeTaskInfo所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeTaskInfoRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeTaskInfoResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskOperationLog(self, request):
        """获取维修任务操作日志

        :param request: 调用DescribeTaskOperationLog所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeTaskOperationLogRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeTaskOperationLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskOperationLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskOperationLogResponse()
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


    def RepairTaskControl(self, request):
        """此接口用于操作维修任务<br>
        入参TaskId为维修任务ID<br>
        入参Operate表示对维修任务的操作，支持如下取值：<br>
        AuthorizeRepair（授权维修）<br>
        Ignore（暂不提醒）<br>
        ConfirmRecovered（维修完成后，确认故障恢复）<br>
        ConfirmUnRecovered（维修完成后，确认故障未恢复）<br>
        <br>
        操作约束（当前任务状态(TaskStatus)->对应可执行的操作）：<br>
        未授权(1)->授权维修；暂不处理<br>
        暂不处理(4)->授权维修<br>
        待确认(3)->确认故障恢复；确认故障未恢复<br>
        未恢复(6)->确认故障恢复<br>
        <br>
        对于Ping不可达故障的任务，还允许：<br>
        未授权->确认故障恢复<br>
        暂不处理->确认故障恢复<br>
        <br>
        处理中与已恢复状态的任务不允许进行操作。<br>
        <br>
        详细信息请访问：https://cloud.tencent.com/document/product/386/18190

        :param request: 调用RepairTaskControl所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.RepairTaskControlRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.RepairTaskControlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RepairTaskControl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RepairTaskControlResponse()
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