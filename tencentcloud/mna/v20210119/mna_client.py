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
from tencentcloud.mna.v20210119 import models


class MnaClient(AbstractClient):
    _apiVersion = '2021-01-19'
    _endpoint = 'mna.tencentcloudapi.com'
    _service = 'mna'


    def AddDevice(self, request):
        """新建设备记录

        :param request: Request instance for AddDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.AddDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.AddDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDeviceResponse()
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


    def CreateQos(self, request):
        """移动网络发起Qos加速过程

        :param request: Request instance for CreateQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.CreateQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.CreateQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateQos", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateQosResponse()
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


    def DeleteDevice(self, request):
        """删除设备信息

        :param request: Request instance for DeleteDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDeviceResponse()
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


    def DeleteQos(self, request):
        """移动网络停止Qos加速过程

        :param request: Request instance for DeleteQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.DeleteQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DeleteQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteQos", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteQosResponse()
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


    def DescribeQos(self, request):
        """获取Qos加速状态

        :param request: Request instance for DescribeQos.
        :type request: :class:`tencentcloud.mna.v20210119.models.DescribeQosRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.DescribeQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQos", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeQosResponse()
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


    def GetDevice(self, request):
        """通过指定设备的ID查找设备详细信息

        :param request: Request instance for GetDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDeviceResponse()
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


    def GetDevices(self, request):
        """获取设备信息列表

        :param request: Request instance for GetDevices.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetDevicesRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetDevicesResponse()
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


    def GetFlowStatistic(self, request):
        """获取指定设备Id，指定时间点数据流量使用情况

        :param request: Request instance for GetFlowStatistic.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetFlowStatisticResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetFlowStatistic", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetFlowStatisticResponse()
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


    def GetStatisticData(self, request):
        """在用量统计页面下载流量数据

        :param request: Request instance for GetStatisticData.
        :type request: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.GetStatisticDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetStatisticData", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetStatisticDataResponse()
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


    def UpdateDevice(self, request):
        """更新设备信息

        :param request: Request instance for UpdateDevice.
        :type request: :class:`tencentcloud.mna.v20210119.models.UpdateDeviceRequest`
        :rtype: :class:`tencentcloud.mna.v20210119.models.UpdateDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDevice", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateDeviceResponse()
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