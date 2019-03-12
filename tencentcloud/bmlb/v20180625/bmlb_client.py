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
from tencentcloud.bmlb.v20180625 import models


class BmlbClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmlb.tencentcloudapi.com'


    def BindL4Backends(self, request):
        """绑定黑石服务器到四层监听器。服务器包括物理服务器、虚拟机以及半托管机器。

        :param request: 调用BindL4Backends所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindL4BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindL4BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindL4Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindL4BackendsResponse()
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


    def BindL7Backends(self, request):
        """绑定黑石物理服务器或半托管服务器到七层转发路径。

        :param request: 调用BindL7Backends所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindL7BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindL7BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindL7Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindL7BackendsResponse()
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


    def BindTrafficMirrorListeners(self, request):
        """绑定黑石服务器七层监听器到流量镜像实例。

        :param request: 调用BindTrafficMirrorListeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindTrafficMirrorListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindTrafficMirrorListenersResponse()
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


    def BindTrafficMirrorReceivers(self, request):
        """绑定黑石物理服务器成为流量镜像接收机。

        :param request: 调用BindTrafficMirrorReceivers所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorReceiversRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.BindTrafficMirrorReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindTrafficMirrorReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindTrafficMirrorReceiversResponse()
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


    def CreateL4Listeners(self, request):
        """创建黑石四层负载均衡监听器功能。黑石负载均衡四层监听器提供了转发用户请求的具体规则，包括端口、协议、会话保持、健康检查等参数。

        :param request: 调用CreateL4Listeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateL4ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateL4ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL4Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL4ListenersResponse()
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


    def CreateL7Listeners(self, request):
        """创建黑石负载均衡七层监听器功能。负载均衡七层监听器提供了转发用户请求的具体规则，包括端口、协议等参数。

        :param request: 调用CreateL7Listeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateL7ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateL7ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7ListenersResponse()
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


    def CreateL7Rules(self, request):
        """创建黑石负载均衡七层转发规则。

        :param request: 调用CreateL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateL7RulesRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateL7RulesResponse()
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


    def CreateLoadBalancers(self, request):
        """用来创建黑石负载均衡。为了使用黑石负载均衡服务，您必须要创建一个或者多个负载均衡实例。通过成功调用该接口，会返回负载均衡实例的唯一ID。用户可以购买的黑石负载均衡实例类型分为：公网类型、内网类型。公网类型负载均衡对应一个BGP VIP，可用于快速访问公网负载均衡绑定的物理服务器；内网类型负载均衡对应一个腾讯云内部的VIP，不能通过Internet访问，可快速访问内网负载均衡绑定的物理服务器。

        :param request: 调用CreateLoadBalancers所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLoadBalancersResponse()
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


    def CreateTrafficMirror(self, request):
        """创建流量镜像实例。

        :param request: 调用CreateTrafficMirror所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.CreateTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.CreateTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTrafficMirror", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTrafficMirrorResponse()
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


    def DeleteL7Domains(self, request):
        """删除黑石负载均衡七层转发域名。

        :param request: 调用DeleteL7Domains所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7DomainsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7DomainsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL7Domains", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL7DomainsResponse()
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


    def DeleteL7Rules(self, request):
        """删除黑石负载均衡七层转发规则。

        :param request: 调用DeleteL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7RulesRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteL7RulesResponse()
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


    def DeleteListeners(self, request):
        """删除黑石负载均衡监听器。

        :param request: 调用DeleteListeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteListenersResponse()
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


    def DeleteLoadBalancer(self, request):
        """删除用户指定的黑石负载均衡实例。

        :param request: 调用DeleteLoadBalancer所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLoadBalancerResponse()
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


    def DeleteTrafficMirror(self, request):
        """删除已创建的黑石流量镜像实例，删除过程是异步执行的，因此需要使用查询任务接口获取删除的结果。

        :param request: 调用DeleteTrafficMirror所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DeleteTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DeleteTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTrafficMirror", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTrafficMirrorResponse()
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


    def DescribeCertDetail(self, request):
        """获取黑石负载均衡证书详情。

        :param request: 调用DescribeCertDetail所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeCertDetailRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeCertDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertDetailResponse()
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


    def DescribeDevicesBindInfo(self, request):
        """查询黑石物理机和虚机以及托管服务器绑定的黑石负载均衡详情。

        :param request: 调用DescribeDevicesBindInfo所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeDevicesBindInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeDevicesBindInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDevicesBindInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesBindInfoResponse()
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


    def DescribeL4Backends(self, request):
        """获取黑石负载均衡四层监听器绑定的主机列表。

        :param request: 调用DescribeL4Backends所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4BackendsResponse()
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


    def DescribeL4ListenerInfo(self, request):
        """查找绑定了某主机或者指定监听器名称的黑石负载均衡四层监听器。

        :param request: 调用DescribeL4ListenerInfo所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenerInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenerInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4ListenerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4ListenerInfoResponse()
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


    def DescribeL4Listeners(self, request):
        """获取黑石负载均衡四层监听器。

        :param request: 调用DescribeL4Listeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL4ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL4Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL4ListenersResponse()
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


    def DescribeL7Backends(self, request):
        """获取黑石负载均衡七层监听器绑定的主机列表

        :param request: 调用DescribeL7Backends所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7BackendsResponse()
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


    def DescribeL7ListenerInfo(self, request):
        """查找绑定了某主机或者有某转发域名黑石负载均衡七层监听器。

        :param request: 调用DescribeL7ListenerInfo所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenerInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenerInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7ListenerInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7ListenerInfoResponse()
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


    def DescribeL7Listeners(self, request):
        """获取黑石负载均衡七层监听器列表信息。

        :param request: 调用DescribeL7Listeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7Listeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7ListenersResponse()
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


    def DescribeL7ListenersEx(self, request):
        """获取指定VPC下的7层监听器(支持模糊匹配)。

        :param request: 调用DescribeL7ListenersEx所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersExRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7ListenersExResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7ListenersEx", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7ListenersExResponse()
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


    def DescribeL7Rules(self, request):
        """获取黑石负载均衡七层转发规则。

        :param request: 调用DescribeL7Rules所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7RulesRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeL7RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeL7Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeL7RulesResponse()
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


    def DescribeLoadBalancerPortInfo(self, request):
        """获取黑石负载均衡端口相关信息。

        :param request: 调用DescribeLoadBalancerPortInfo所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerPortInfoRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerPortInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerPortInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancerPortInfoResponse()
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


    def DescribeLoadBalancerTaskResult(self, request):
        """查询负载均衡实例异步任务的执行情况。

        :param request: 调用DescribeLoadBalancerTaskResult所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerTaskResultRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancerTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancerTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancerTaskResultResponse()
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


    def DescribeLoadBalancers(self, request):
        """获取黑石负载均衡实例列表

        :param request: 调用DescribeLoadBalancers所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLoadBalancers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLoadBalancersResponse()
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


    def DescribeTrafficMirrorListeners(self, request):
        """获取流量镜像的监听器列表信息。

        :param request: 调用DescribeTrafficMirrorListeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrorListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorListenersResponse()
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


    def DescribeTrafficMirrorReceiverHealthStatus(self, request):
        """获取流量镜像接收机健康状态。

        :param request: 调用DescribeTrafficMirrorReceiverHealthStatus所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiverHealthStatusRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiverHealthStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrorReceiverHealthStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorReceiverHealthStatusResponse()
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


    def DescribeTrafficMirrorReceivers(self, request):
        """获取指定流量镜像实例的接收机信息。

        :param request: 调用DescribeTrafficMirrorReceivers所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiversRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrorReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorReceiversResponse()
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


    def DescribeTrafficMirrors(self, request):
        """获取流量镜像实例的列表信息。

        :param request: 调用DescribeTrafficMirrors所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.DescribeTrafficMirrorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTrafficMirrors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTrafficMirrorsResponse()
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


    def ModifyL4BackendPort(self, request):
        """修改黑石负载均衡四层监听器后端实例端口。

        :param request: 调用ModifyL4BackendPort所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendPortRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4BackendPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4BackendPortResponse()
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


    def ModifyL4BackendProbePort(self, request):
        """修改黑石负载均衡四层监听器后端探测端口。

        :param request: 调用ModifyL4BackendProbePort所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendProbePortRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendProbePortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4BackendProbePort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4BackendProbePortResponse()
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


    def ModifyL4BackendWeight(self, request):
        """修改黑石负载均衡四层监听器后端实例权重功能。

        :param request: 调用ModifyL4BackendWeight所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendWeightRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4BackendWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4BackendWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4BackendWeightResponse()
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


    def ModifyL4Listener(self, request):
        """修改黑石负载均衡四层监听器。

        :param request: 调用ModifyL4Listener所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4ListenerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL4ListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL4Listener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL4ListenerResponse()
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


    def ModifyL7BackendPort(self, request):
        """修改黑石负载均衡七层转发路径后端实例端口。

        :param request: 调用ModifyL7BackendPort所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendPortRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendPortResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7BackendPort", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7BackendPortResponse()
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


    def ModifyL7BackendWeight(self, request):
        """修改黑石负载均衡七层转发路径后端实例权重。

        :param request: 调用ModifyL7BackendWeight所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendWeightRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7BackendWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7BackendWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7BackendWeightResponse()
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


    def ModifyL7Listener(self, request):
        """修改黑石负载均衡七层监听器。

        :param request: 调用ModifyL7Listener所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7ListenerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7ListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7Listener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7ListenerResponse()
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


    def ModifyL7Locations(self, request):
        """修改黑石负载均衡七层转发路径。

        :param request: 调用ModifyL7Locations所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7LocationsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyL7LocationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyL7Locations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyL7LocationsResponse()
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


    def ModifyLoadBalancer(self, request):
        """根据输入参数来修改黑石负载均衡实例的基本配置信息。可能的信息包括负载均衡实例的名称，域名前缀。

        :param request: 调用ModifyLoadBalancer所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancerResponse()
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


    def ModifyLoadBalancerChargeMode(self, request):
        """更改黑石负载均衡的计费方式

        :param request: 调用ModifyLoadBalancerChargeMode所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerChargeModeRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ModifyLoadBalancerChargeModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLoadBalancerChargeMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLoadBalancerChargeModeResponse()
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


    def ReplaceCert(self, request):
        """更新黑石负载均衡证书。

        :param request: 调用ReplaceCert所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.ReplaceCertRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.ReplaceCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceCertResponse()
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


    def SetTrafficMirrorAlias(self, request):
        """设置流量镜像的别名。

        :param request: 调用SetTrafficMirrorAlias所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorAliasRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTrafficMirrorAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTrafficMirrorAliasResponse()
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


    def SetTrafficMirrorHealthSwitch(self, request):
        """设置流量镜像的健康检查参数。

        :param request: 调用SetTrafficMirrorHealthSwitch所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorHealthSwitchRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.SetTrafficMirrorHealthSwitchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetTrafficMirrorHealthSwitch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetTrafficMirrorHealthSwitchResponse()
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


    def UnbindL4Backends(self, request):
        """解绑黑石负载均衡四层监听器物理服务器。

        :param request: 调用UnbindL4Backends所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindL4BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindL4BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindL4Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindL4BackendsResponse()
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


    def UnbindL7Backends(self, request):
        """解绑黑石物理服务器或者托管服务器到七层转发路径功能。

        :param request: 调用UnbindL7Backends所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindL7BackendsRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindL7BackendsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindL7Backends", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindL7BackendsResponse()
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


    def UnbindTrafficMirrorListeners(self, request):
        """解绑流量镜像监听器。

        :param request: 调用UnbindTrafficMirrorListeners所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorListenersRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindTrafficMirrorListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindTrafficMirrorListenersResponse()
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


    def UnbindTrafficMirrorReceivers(self, request):
        """从流量镜像实例上解绑流量镜像接收机。

        :param request: 调用UnbindTrafficMirrorReceivers所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorReceiversRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UnbindTrafficMirrorReceiversResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnbindTrafficMirrorReceivers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindTrafficMirrorReceiversResponse()
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


    def UploadCert(self, request):
        """创建黑石负载均衡证书。

        :param request: 调用UploadCert所需参数的结构体。
        :type request: :class:`tencentcloud.bmlb.v20180625.models.UploadCertRequest`
        :rtype: :class:`tencentcloud.bmlb.v20180625.models.UploadCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UploadCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UploadCertResponse()
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