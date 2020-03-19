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
from tencentcloud.ecm.v20190719 import models


class EcmClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'ecm.tencentcloudapi.com'


    def CreateModule(self, request):
        """创建模块

        :param request: Request instance for CreateModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateModuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateModule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateModuleResponse()
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


    def DeleteImage(self, request):
        """删除镜像

        :param request: Request instance for DeleteImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageResponse()
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


    def DeleteModule(self, request):
        """删除业务模块

        :param request: Request instance for DeleteModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteModuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteModule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteModuleResponse()
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


    def DescribeBaseOverview(self, request):
        """获取概览页统计的基本数据

        :param request: Request instance for DescribeBaseOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeBaseOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeBaseOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBaseOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBaseOverviewResponse()
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


    def DescribeConfig(self, request):
        """获取带宽硬盘等数据的限制

        :param request: Request instance for DescribeConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeConfigResponse()
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


    def DescribeImage(self, request):
        """展示镜像列表

        :param request: Request instance for DescribeImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageResponse()
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


    def DescribeInstanceTypeConfig(self, request):
        """获取机型配置列表

        :param request: Request instance for DescribeInstanceTypeConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceTypeConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceTypeConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceTypeConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTypeConfigResponse()
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
        """获取实例的相关信息。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesResponse`

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


    def DescribeInstancesDeniedActions(self, request):
        """通过实例id获取当前禁止的操作

        :param request: Request instance for DescribeInstancesDeniedActions.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesDeniedActionsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstancesDeniedActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesDeniedActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesDeniedActionsResponse()
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


    def DescribeModule(self, request):
        """获取模块列表

        :param request: Request instance for DescribeModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModuleResponse()
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


    def DescribeModuleDetail(self, request):
        """展示模块详细信息

        :param request: Request instance for DescribeModuleDetail.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleDetailRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeModuleDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModuleDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModuleDetailResponse()
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


    def DescribeNode(self, request):
        """获取节点列表

        :param request: Request instance for DescribeNode.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNodeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNodeResponse()
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


    def DescribePeakBaseOverview(self, request):
        """CPU 内存 硬盘等基础信息峰值数据

        :param request: Request instance for DescribePeakBaseOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePeakBaseOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePeakBaseOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePeakBaseOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePeakBaseOverviewResponse()
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


    def DescribePeakNetworkOverview(self, request):
        """获取网络峰值数据

        :param request: Request instance for DescribePeakNetworkOverview.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePeakNetworkOverviewRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePeakNetworkOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePeakNetworkOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePeakNetworkOverviewResponse()
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


    def ModifyInstancesAttribute(self, request):
        """修改实例的属性。

        :param request: Request instance for ModifyInstancesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesAttributeResponse()
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


    def ModifyModuleImage(self, request):
        """ModifyModuleImage

        :param request: Request instance for ModifyModuleImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleImageResponse()
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


    def ModifyModuleName(self, request):
        """修改模块名称

        :param request: Request instance for ModifyModuleName.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNameRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleNameResponse()
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


    def ModifyModuleNetwork(self, request):
        """修改模块默认带宽上限

        :param request: Request instance for ModifyModuleNetwork.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNetworkRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleNetworkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleNetwork", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleNetworkResponse()
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


    def RebootInstances(self, request):
        """只有状态为RUNNING的实例才可以进行此操作；接口调用成功时，实例会进入REBOOTING状态；重启实例成功时，实例会进入RUNNING状态；支持强制重启，强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebootInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebootInstancesResponse()
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


    def ResetInstances(self, request):
        """重装实例，若指定了ImageId参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装；若未指定密码，则密码通过站内信形式随后发送。

        :param request: Request instance for ResetInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesResponse()
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


    def ResetInstancesMaxBandwidth(self, request):
        """重置实例的最大带宽上限。

        :param request: Request instance for ResetInstancesMaxBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesMaxBandwidthResponse()
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


    def TerminateInstances(self, request):
        """销毁实例

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateInstancesResponse()
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