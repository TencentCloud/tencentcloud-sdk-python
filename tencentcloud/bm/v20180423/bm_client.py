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
from tencentcloud.bm.v20180423 import models


class BmClient(AbstractClient):
    _apiVersion = '2018-04-23'
    _endpoint = 'bm.tencentcloudapi.com'


    def BindPsaTag(self, request):
        """为预授权规则绑定标签

        :param request: 调用BindPsaTag所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.BindPsaTagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.BindPsaTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindPsaTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindPsaTagResponse()
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


    def CreatePsaRegulation(self, request):
        """创建预授权规则

        :param request: 调用CreatePsaRegulation所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreatePsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreatePsaRegulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePsaRegulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePsaRegulationResponse()
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


    def CreateSpotDevice(self, request):
        """创建黑石竞价实例

        :param request: 调用CreateSpotDevice所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateSpotDeviceRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateSpotDeviceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSpotDevice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSpotDeviceResponse()
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


    def CreateUserCmd(self, request):
        """创建自定义脚本

        :param request: 调用CreateUserCmd所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.CreateUserCmdRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.CreateUserCmdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUserCmd", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserCmdResponse()
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


    def DeletePsaRegulation(self, request):
        """删除预授权规则

        :param request: 调用DeletePsaRegulation所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.DeletePsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DeletePsaRegulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePsaRegulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePsaRegulationResponse()
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


    def DescribeDevices(self, request):
        """查询物理服务器，可以按照实例，业务IP等过滤

        :param request: 调用DescribeDevices所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevices", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
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


    def DescribePsaRegulations(self, request):
        """获取预授权规则列表

        :param request: 调用DescribePsaRegulations所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.DescribePsaRegulationsRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.DescribePsaRegulationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePsaRegulations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePsaRegulationsResponse()
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


    def ModifyPsaRegulation(self, request):
        """允许修改规则信息及关联故障类型

        :param request: 调用ModifyPsaRegulation所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.ModifyPsaRegulationRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.ModifyPsaRegulationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPsaRegulation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPsaRegulationResponse()
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


    def UnbindPsaTag(self, request):
        """解除标签与预授权规则的绑定

        :param request: 调用UnbindPsaTag所需参数的结构体。
        :type request: :class:`tencentcloud.bm.v20180423.models.UnbindPsaTagRequest`
        :rtype: :class:`tencentcloud.bm.v20180423.models.UnbindPsaTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindPsaTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindPsaTagResponse()
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