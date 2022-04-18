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
from tencentcloud.bmeip.v20180625 import models


class BmeipClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmeip.tencentcloudapi.com'
    _service = 'bmeip'


    def BindEipAcls(self, request):
        """此接口用于为某个 EIP 关联 ACL。

        :param request: Request instance for BindEipAcls.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.BindEipAclsRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.BindEipAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindEipAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindEipAclsResponse()
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


    def BindHosted(self, request):
        """BindHosted接口用于绑定黑石弹性公网IP到黑石托管机器上

        :param request: Request instance for BindHosted.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.BindHostedRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.BindHostedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindHosted", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindHostedResponse()
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


    def BindRs(self, request):
        """绑定黑石EIP

        :param request: Request instance for BindRs.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.BindRsRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.BindRsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindRs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRsResponse()
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


    def BindVpcIp(self, request):
        """黑石EIP绑定VPCIP

        :param request: Request instance for BindVpcIp.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.BindVpcIpRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.BindVpcIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindVpcIp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindVpcIpResponse()
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


    def CreateEip(self, request):
        """创建黑石弹性公网IP

        :param request: Request instance for CreateEip.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.CreateEipRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.CreateEipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEip", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEipResponse()
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


    def CreateEipAcl(self, request):
        """创建黑石弹性公网 EIPACL

        :param request: Request instance for CreateEipAcl.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.CreateEipAclRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.CreateEipAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateEipAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEipAclResponse()
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


    def DeleteEip(self, request):
        """释放黑石弹性公网IP

        :param request: Request instance for DeleteEip.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.DeleteEipRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.DeleteEipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEip", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEipResponse()
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


    def DeleteEipAcl(self, request):
        """删除弹性公网IP ACL

        :param request: Request instance for DeleteEipAcl.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.DeleteEipAclRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.DeleteEipAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteEipAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteEipAclResponse()
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


    def DescribeEipAcls(self, request):
        """查询弹性公网IP ACL

        :param request: Request instance for DescribeEipAcls.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipAclsRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEipAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipAclsResponse()
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


    def DescribeEipQuota(self, request):
        """查询黑石EIP 限额

        :param request: Request instance for DescribeEipQuota.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipQuotaRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEipQuota", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipQuotaResponse()
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


    def DescribeEipTask(self, request):
        """黑石EIP查询任务状态

        :param request: Request instance for DescribeEipTask.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipTaskRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEipTask", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipTaskResponse()
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


    def DescribeEips(self, request):
        """黑石EIP查询接口

        :param request: Request instance for DescribeEips.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipsRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.DescribeEipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEips", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEipsResponse()
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


    def ModifyEipAcl(self, request):
        """修改弹性公网IP ACL

        :param request: Request instance for ModifyEipAcl.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.ModifyEipAclRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.ModifyEipAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEipAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEipAclResponse()
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


    def ModifyEipCharge(self, request):
        """黑石EIP修改计费方式

        :param request: Request instance for ModifyEipCharge.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.ModifyEipChargeRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.ModifyEipChargeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEipCharge", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEipChargeResponse()
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


    def ModifyEipName(self, request):
        """更新黑石EIP名称

        :param request: Request instance for ModifyEipName.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.ModifyEipNameRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.ModifyEipNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyEipName", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyEipNameResponse()
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


    def UnbindEipAcls(self, request):
        """解绑弹性公网IP ACL

        :param request: Request instance for UnbindEipAcls.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.UnbindEipAclsRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.UnbindEipAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindEipAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindEipAclsResponse()
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


    def UnbindHosted(self, request):
        """UnbindHosted接口用于解绑托管机器上的EIP

        :param request: Request instance for UnbindHosted.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.UnbindHostedRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.UnbindHostedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindHosted", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindHostedResponse()
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


    def UnbindRs(self, request):
        """解绑黑石EIP

        :param request: Request instance for UnbindRs.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.UnbindRsRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.UnbindRsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindRs", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindRsResponse()
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


    def UnbindRsList(self, request):
        """批量解绑物理机弹性公网IP接口

        :param request: Request instance for UnbindRsList.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.UnbindRsListRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.UnbindRsListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindRsList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindRsListResponse()
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


    def UnbindVpcIp(self, request):
        """黑石EIP解绑VPCIP

        :param request: Request instance for UnbindVpcIp.
        :type request: :class:`tencentcloud.bmeip.v20180625.models.UnbindVpcIpRequest`
        :rtype: :class:`tencentcloud.bmeip.v20180625.models.UnbindVpcIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindVpcIp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindVpcIpResponse()
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