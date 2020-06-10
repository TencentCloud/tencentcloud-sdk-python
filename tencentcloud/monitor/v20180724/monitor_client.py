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
from tencentcloud.monitor.v20180724 import models


class MonitorClient(AbstractClient):
    _apiVersion = '2018-07-24'
    _endpoint = 'monitor.tencentcloudapi.com'


    def BindingPolicyObject(self, request):
        """将告警策略绑定到特定对象

        :param request: Request instance for BindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.BindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindingPolicyObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindingPolicyObjectResponse()
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


    def CreatePolicyGroup(self, request):
        """增加策略组

        :param request: Request instance for CreatePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.CreatePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePolicyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePolicyGroupResponse()
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


    def DeletePolicyGroup(self, request):
        """删除告警策略组

        :param request: Request instance for DeletePolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DeletePolicyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePolicyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePolicyGroupResponse()
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


    def DescribeAccidentEventList(self, request):
        """获取平台事件列表

        :param request: Request instance for DescribeAccidentEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeAccidentEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccidentEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccidentEventListResponse()
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


    def DescribeBaseMetrics(self, request):
        """获取基础指标详情

        :param request: Request instance for DescribeBaseMetrics.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBaseMetricsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBaseMetrics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaseMetricsResponse()
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


    def DescribeBasicAlarmList(self, request):
        """获取基础告警列表

        :param request: Request instance for DescribeBasicAlarmList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBasicAlarmListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBasicAlarmList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBasicAlarmListResponse()
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


    def DescribeBindingPolicyObjectList(self, request):
        """获取已绑定对象列表

        :param request: Request instance for DescribeBindingPolicyObjectList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeBindingPolicyObjectListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBindingPolicyObjectList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBindingPolicyObjectListResponse()
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


    def DescribePolicyConditionList(self, request):
        """获取基础告警策略条件

        :param request: Request instance for DescribePolicyConditionList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyConditionListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyConditionList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyConditionListResponse()
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


    def DescribePolicyGroupInfo(self, request):
        """获取基础策略组详情

        :param request: Request instance for DescribePolicyGroupInfo.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyGroupInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyGroupInfoResponse()
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


    def DescribePolicyGroupList(self, request):
        """获取基础策略告警组列表

        :param request: Request instance for DescribePolicyGroupList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribePolicyGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePolicyGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePolicyGroupListResponse()
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


    def DescribeProductEventList(self, request):
        """分页获取产品事件的列表

        :param request: Request instance for DescribeProductEventList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeProductEventListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductEventList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductEventListResponse()
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


    def DescribeProductList(self, request):
        """查询云监控产品列表

        :param request: Request instance for DescribeProductList.
        :type request: :class:`tencentcloud.monitor.v20180724.models.DescribeProductListRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.DescribeProductListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductListResponse()
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


    def GetMonitorData(self, request):
        """获取云产品的监控数据。传入产品的命名空间、对象维度描述和监控指标即可获得相应的监控数据。
        接口调用频率限制为：20次/秒，1200次/分钟。单请求最多可支持批量拉取10个实例的监控数据，单请求的数据点数限制为1440个。
        若您需要调用的指标、对象较多，可能存在因限频出现拉取失败的情况，建议尽量将请求按时间维度均摊。

        :param request: Request instance for GetMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.GetMonitorDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetMonitorData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetMonitorDataResponse()
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


    def ModifyAlarmReceivers(self, request):
        """修改告警接收人

        :param request: Request instance for ModifyAlarmReceivers.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyAlarmReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAlarmReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAlarmReceiversResponse()
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


    def ModifyPolicyGroup(self, request):
        """更新策略组

        :param request: Request instance for ModifyPolicyGroup.
        :type request: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.ModifyPolicyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPolicyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPolicyGroupResponse()
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


    def PutMonitorData(self, request):
        """默认接口请求频率限制：50次/秒。
        默认单租户指标上限：100个。
        单次上报最多 30 个指标/值对，请求返回错误时，请求中所有的指标/值均不会被保存。

        上报的时间戳为期望保存的时间戳，建议构造整数分钟时刻的时间戳。
        时间戳时间范围必须为当前时间到 300 秒前之间。
        同一 IP 指标对的数据需按分钟先后顺序上报。

        :param request: Request instance for PutMonitorData.
        :type request: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.PutMonitorDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutMonitorData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutMonitorDataResponse()
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


    def SendCustomAlarmMsg(self, request):
        """发送自定义消息告警

        :param request: Request instance for SendCustomAlarmMsg.
        :type request: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.SendCustomAlarmMsgResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendCustomAlarmMsg", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendCustomAlarmMsgResponse()
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


    def UnBindingAllPolicyObject(self, request):
        """删除全部的关联对象

        :param request: Request instance for UnBindingAllPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingAllPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindingAllPolicyObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindingAllPolicyObjectResponse()
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


    def UnBindingPolicyObject(self, request):
        """删除策略的关联对象

        :param request: Request instance for UnBindingPolicyObject.
        :type request: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectRequest`
        :rtype: :class:`tencentcloud.monitor.v20180724.models.UnBindingPolicyObjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnBindingPolicyObject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnBindingPolicyObjectResponse()
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