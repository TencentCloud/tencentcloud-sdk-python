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
from tencentcloud.tem.v20201221 import models


class TemClient(AbstractClient):
    _apiVersion = '2020-12-21'
    _endpoint = 'tem.tencentcloudapi.com'
    _service = 'tem'


    def CreateCosToken(self, request):
        """生成Cos临时秘钥

        :param request: Request instance for CreateCosToken.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCosToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosTokenResponse()
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


    def CreateCosTokenV2(self, request):
        """生成Cos临时秘钥

        :param request: Request instance for CreateCosTokenV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateCosTokenV2Response`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCosTokenV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCosTokenV2Response()
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


    def CreateNamespace(self, request):
        """创建环境

        :param request: Request instance for CreateNamespace.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateNamespaceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNamespaceResponse()
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


    def CreateResource(self, request):
        """绑定云资源

        :param request: Request instance for CreateResource.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateResourceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateResourceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateResource", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateResourceResponse()
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


    def CreateServiceV2(self, request):
        """创建服务

        :param request: Request instance for CreateServiceV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.CreateServiceV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.CreateServiceV2Response`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceV2Response()
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


    def DeleteIngress(self, request):
        """删除 Ingress 规则

        :param request: Request instance for DeleteIngress.
        :type request: :class:`tencentcloud.tem.v20201221.models.DeleteIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DeleteIngressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIngress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIngressResponse()
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


    def DeployServiceV2(self, request):
        """服务部署

        :param request: Request instance for DeployServiceV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.DeployServiceV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DeployServiceV2Response`

        """
        try:
            params = request._serialize()
            body = self.call("DeployServiceV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployServiceV2Response()
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


    def DescribeIngress(self, request):
        """查询 Ingress 规则

        :param request: Request instance for DescribeIngress.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeIngressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIngress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIngressResponse()
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


    def DescribeIngresses(self, request):
        """查询 Ingress 规则列表

        :param request: Request instance for DescribeIngresses.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeIngressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIngresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIngressesResponse()
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


    def DescribeNamespaces(self, request):
        """获取租户环境列表

        :param request: Request instance for DescribeNamespaces.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeNamespacesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeNamespacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNamespaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNamespacesResponse()
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


    def DescribeRelatedIngresses(self, request):
        """查询服务关联的 Ingress 规则列表

        :param request: Request instance for DescribeRelatedIngresses.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeRelatedIngressesRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeRelatedIngressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRelatedIngresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRelatedIngressesResponse()
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


    def DescribeServiceRunPodListV2(self, request):
        """获取服务下面运行pod列表

        :param request: Request instance for DescribeServiceRunPodListV2.
        :type request: :class:`tencentcloud.tem.v20201221.models.DescribeServiceRunPodListV2Request`
        :rtype: :class:`tencentcloud.tem.v20201221.models.DescribeServiceRunPodListV2Response`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceRunPodListV2", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceRunPodListV2Response()
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


    def ModifyIngress(self, request):
        """创建或者更新 Ingress 规则

        :param request: Request instance for ModifyIngress.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyIngressRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyIngressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIngress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIngressResponse()
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


    def ModifyNamespace(self, request):
        """编辑环境

        :param request: Request instance for ModifyNamespace.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyNamespaceRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyNamespaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNamespace", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNamespaceResponse()
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


    def ModifyServiceInfo(self, request):
        """修改服务基本信息

        :param request: Request instance for ModifyServiceInfo.
        :type request: :class:`tencentcloud.tem.v20201221.models.ModifyServiceInfoRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.ModifyServiceInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceInfoResponse()
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


    def RestartServiceRunPod(self, request):
        """重启实例

        :param request: Request instance for RestartServiceRunPod.
        :type request: :class:`tencentcloud.tem.v20201221.models.RestartServiceRunPodRequest`
        :rtype: :class:`tencentcloud.tem.v20201221.models.RestartServiceRunPodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartServiceRunPod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartServiceRunPodResponse()
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