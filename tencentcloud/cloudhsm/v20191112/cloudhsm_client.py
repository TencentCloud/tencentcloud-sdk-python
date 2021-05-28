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
from tencentcloud.cloudhsm.v20191112 import models


class CloudhsmClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'cloudhsm.tencentcloudapi.com'
    _service = 'cloudhsm'


    def DescribeHSMBySubnetId(self, request):
        """通过SubnetId获取Hsm资源数

        :param request: Request instance for DescribeHSMBySubnetId.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMBySubnetIdRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMBySubnetIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHSMBySubnetId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHSMBySubnetIdResponse()
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


    def DescribeHSMByVpcId(self, request):
        """通过VpcId获取Hsm资源数

        :param request: Request instance for DescribeHSMByVpcId.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMByVpcIdRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeHSMByVpcIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHSMByVpcId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHSMByVpcIdResponse()
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


    def DescribeSubnet(self, request):
        """查询子网列表

        :param request: Request instance for DescribeSubnet.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSubnetRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetResponse()
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


    def DescribeSupportedHsm(self, request):
        """获取当前地域所支持的设备列表

        :param request: Request instance for DescribeSupportedHsm.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSupportedHsmRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeSupportedHsmResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSupportedHsm", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSupportedHsmResponse()
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


    def DescribeUsg(self, request):
        """根据用户的AppId获取用户安全组列表

        :param request: Request instance for DescribeUsg.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsg", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsgResponse()
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


    def DescribeUsgRule(self, request):
        """获取安全组详情

        :param request: Request instance for DescribeUsgRule.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgRuleRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeUsgRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUsgRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsgRuleResponse()
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


    def DescribeVpc(self, request):
        """查询用户的私有网络列表

        :param request: Request instance for DescribeVpc.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVpcRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcResponse()
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


    def DescribeVsmAttributes(self, request):
        """获取VSM属性

        :param request: Request instance for DescribeVsmAttributes.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmAttributesRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVsmAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVsmAttributesResponse()
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


    def DescribeVsms(self, request):
        """获取用户VSM列表

        :param request: Request instance for DescribeVsms.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmsRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.DescribeVsmsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVsms", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVsmsResponse()
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


    def InquiryPriceBuyVsm(self, request):
        """购买询价接口

        :param request: Request instance for InquiryPriceBuyVsm.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.InquiryPriceBuyVsmRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.InquiryPriceBuyVsmResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceBuyVsm", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceBuyVsmResponse()
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


    def ModifyVsmAttributes(self, request):
        """修改VSM属性

        :param request: Request instance for ModifyVsmAttributes.
        :type request: :class:`tencentcloud.cloudhsm.v20191112.models.ModifyVsmAttributesRequest`
        :rtype: :class:`tencentcloud.cloudhsm.v20191112.models.ModifyVsmAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVsmAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVsmAttributesResponse()
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