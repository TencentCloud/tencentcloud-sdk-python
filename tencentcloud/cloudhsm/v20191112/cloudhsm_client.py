# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
from tencentcloud.cloudhsm.v20191112 import models


class CloudhsmClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'cloudhsm.tencentcloudapi.com'
    _service = 'cloudhsm'


    def DescribeHSMBySubnetId(self, request):
        r"""通过SubnetId获取Hsm资源数

        :param request: Request instance for DescribeHSMBySubnetId.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMBySubnetIdRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMBySubnetIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHSMBySubnetId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHSMBySubnetIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHSMByVpcId(self, request):
        r"""通过VpcId获取Hsm资源数

        :param request: Request instance for DescribeHSMByVpcId.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMByVpcIdRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMByVpcIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHSMByVpcId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHSMByVpcIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnet(self, request):
        r"""查询子网列表

        :param request: Request instance for DescribeSubnet.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSubnetRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSupportedHsm(self, request):
        r"""获取当前地域所支持的设备列表

        :param request: Request instance for DescribeSupportedHsm.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSupportedHsmRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSupportedHsmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSupportedHsm", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSupportedHsmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsg(self, request):
        r"""根据用户的AppId获取用户安全组列表

        :param request: Request instance for DescribeUsg.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsg", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsgResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsgRule(self, request):
        r"""获取安全组详情

        :param request: Request instance for DescribeUsgRule.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgRuleRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsgRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsgRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpc(self, request):
        r"""查询用户的私有网络列表

        :param request: Request instance for DescribeVpc.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVpcRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVsmAttributes(self, request):
        r"""获取VSM属性

        :param request: Request instance for DescribeVsmAttributes.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmAttributesRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVsmAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVsmAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVsms(self, request):
        r"""获取用户VSM列表

        :param request: Request instance for DescribeVsms.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmsRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVsms", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVsmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAlarmEvent(self, request):
        r"""获取告警事件

        :param request: Request instance for GetAlarmEvent.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.GetAlarmEventRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.GetAlarmEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAlarmEvent", params, headers=headers)
            response = json.loads(body)
            model = models.GetAlarmEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetVsmMonitorInfo(self, request):
        r"""获取VSM监控信息

        :param request: Request instance for GetVsmMonitorInfo.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.GetVsmMonitorInfoRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.GetVsmMonitorInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetVsmMonitorInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetVsmMonitorInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceBuyVsm(self, request):
        r"""购买询价接口

        :param request: Request instance for InquiryPriceBuyVsm.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.InquiryPriceBuyVsmRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.InquiryPriceBuyVsmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceBuyVsm", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceBuyVsmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAlarmEvent(self, request):
        r"""修改告警事件

        :param request: Request instance for ModifyAlarmEvent.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.ModifyAlarmEventRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.ModifyAlarmEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAlarmEvent", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAlarmEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVsmAttributes(self, request):
        r"""修改VSM属性

        :param request: Request instance for ModifyVsmAttributes.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.ModifyVsmAttributesRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.ModifyVsmAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVsmAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVsmAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))