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
from tencentcloud.gaap.v20180529 import models


class GaapClient(AbstractClient):
    _apiVersion = '2018-05-29'
    _endpoint = 'gaap.tencentcloudapi.com'


    def AddRealServers(self, request):
        """添加源站(服务器)信息，支持IP或域名

        :param request: 调用AddRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.AddRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.AddRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddRealServersResponse()
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


    def BindListenerRealServers(self, request):
        """本接口（BindListenerRealServers）用于TCP/UDP监听器绑定解绑源站。
        注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。例如：原来绑定的源站为A，B，C，本次调用的选择绑定的源站为C，D，E，那么调用后所绑定的源站为C，D，E。

        :param request: 调用BindListenerRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.BindListenerRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.BindListenerRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindListenerRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindListenerRealServersResponse()
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


    def BindRuleRealServers(self, request):
        """该接口用于7层监听器的转发规则绑定源站。注意：本接口会解绑之前绑定的源站，绑定本次调用所选择的源站。

        :param request: 调用BindRuleRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.BindRuleRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.BindRuleRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("BindRuleRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindRuleRealServersResponse()
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


    def CheckProxyCreate(self, request):
        """本接口(CheckProxyCreate)用于查询能否创建指定配置的加速通道。

        :param request: 调用CheckProxyCreate所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CheckProxyCreateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CheckProxyCreateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckProxyCreate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckProxyCreateResponse()
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


    def CloseProxies(self, request):
        """本接口（CloseProxies）用于关闭通道。通道关闭后，不再产生流量，但每天仍然收取通道基础配置费用。

        :param request: 调用CloseProxies所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CloseProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CloseProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseProxiesResponse()
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


    def CloseSecurityPolicy(self, request):
        """关闭安全策略

        :param request: 调用CloseSecurityPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CloseSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CloseSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseSecurityPolicyResponse()
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


    def CreateCertificate(self, request):
        """本接口（CreateCertificate）用于创建Gaap相关证书和配置文件，包括基础认证配置文件，客户端CA证书，服务器SSL证书，Gaap SSL证书以及源站CA证书。

        :param request: 调用CreateCertificate所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateCertificateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCertificateResponse()
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


    def CreateDomain(self, request):
        """本接口（CreateDomain）用于创建HTTP/HTTPS监听器的访问域名，客户端请求通过访问该域名来请求后端业务。
        该接口仅支持version3.0的通道。

        :param request: 调用CreateDomain所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDomainResponse()
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


    def CreateHTTPListener(self, request):
        """该接口（CreateHTTPListener）用于在通道实例下创建HTTP协议类型的监听器。

        :param request: 调用CreateHTTPListener所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPListenerRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHTTPListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHTTPListenerResponse()
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


    def CreateHTTPSListener(self, request):
        """该接口（CreateHTTPSListener）用于在通道实例下创建HTTPS协议类型的监听器。

        :param request: 调用CreateHTTPSListener所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPSListenerRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateHTTPSListenerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHTTPSListener", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHTTPSListenerResponse()
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


    def CreateProxy(self, request):
        """本接口（CreateProxy）用于创建/复制一个指定配置的加速通道。当复制通道时，需要设置新通道的基本配置参数，并设置ClonedProxyId来指定被复制的通道。

        :param request: 调用CreateProxy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProxyResponse()
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


    def CreateProxyGroup(self, request):
        """本接口（CreateProxyGroup）用于创建通道组。

        :param request: 调用CreateProxyGroup所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProxyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProxyGroupResponse()
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


    def CreateProxyGroupDomain(self, request):
        """本接口（CreateProxyGroupDomain）用于创建通道组域名，并开启域名解析。

        :param request: 调用CreateProxyGroupDomain所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateProxyGroupDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateProxyGroupDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateProxyGroupDomainResponse()
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


    def CreateRule(self, request):
        """该接口（CreateRule）用于创建HTTP/HTTPS监听器转发规则。

        :param request: 调用CreateRule所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRuleResponse()
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


    def CreateSecurityPolicy(self, request):
        """创建安全策略

        :param request: 调用CreateSecurityPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityPolicyResponse()
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


    def CreateSecurityRules(self, request):
        """添加安全策略规则

        :param request: 调用CreateSecurityRules所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityRulesResponse()
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


    def CreateTCPListeners(self, request):
        """该接口（CreateTCPListeners）用于批量创建单通道或者通道组的TCP协议类型的监听器。

        :param request: 调用CreateTCPListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateTCPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateTCPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTCPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTCPListenersResponse()
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


    def CreateUDPListeners(self, request):
        """该接口（CreateUDPListeners）用于批量创建单通道或者通道组的UDP协议类型的监听器。

        :param request: 调用CreateUDPListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.CreateUDPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.CreateUDPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateUDPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUDPListenersResponse()
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


    def DeleteCertificate(self, request):
        """本接口（DeleteCertificate）用于删除证书。

        :param request: 调用DeleteCertificate所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteCertificateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCertificateResponse()
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


    def DeleteDomain(self, request):
        """本接口（DeleteDomain）仅适用于7层监听器，用于删除该监听器下对应域名及域名下的所有规则，所有已绑定源站的规则将自动解绑。

        :param request: 调用DeleteDomain所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDomainResponse()
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
        """该接口（DeleteListeners）用于批量删除通道或通道组的监听器，包括4/7层监听器。

        :param request: 调用DeleteListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteListenersResponse`

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


    def DeleteProxyGroup(self, request):
        """本接口（DeleteProxyGroup）用于删除通道组。

        :param request: 调用DeleteProxyGroup所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteProxyGroupRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteProxyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteProxyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteProxyGroupResponse()
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


    def DeleteRule(self, request):
        """该接口（DeleteRule）用于删除HTTP/HTTPS监听器的转发规则。

        :param request: 调用DeleteRule所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRuleResponse()
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


    def DeleteSecurityPolicy(self, request):
        """删除安全策略

        :param request: 调用DeleteSecurityPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityPolicyResponse()
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


    def DeleteSecurityRules(self, request):
        """删除安全策略规则

        :param request: 调用DeleteSecurityRules所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DeleteSecurityRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityRulesResponse()
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


    def DescribeAccessRegions(self, request):
        """本接口（DescribeAccessRegions）用于查询加速区域，即客户端接入区域。

        :param request: 调用DescribeAccessRegions所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRegionsResponse()
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


    def DescribeAccessRegionsByDestRegion(self, request):
        """本接口（DescribeAccessRegionsByDestRegion）根据源站区域查询可用的加速区域列表

        :param request: 调用DescribeAccessRegionsByDestRegion所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsByDestRegionRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeAccessRegionsByDestRegionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRegionsByDestRegion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRegionsByDestRegionResponse()
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


    def DescribeCertificateDetail(self, request):
        """本接口（DescribeCertificateDetail）用于查询证书详情，包括证书ID，证书名字，证书类型，证书内容以及密钥等信息。

        :param request: 调用DescribeCertificateDetail所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificateDetailRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificateDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificateDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificateDetailResponse()
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


    def DescribeCertificates(self, request):
        """本接口（DescribeCertificates）用来查询可以使用的证书列表。

        :param request: 调用DescribeCertificates所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificatesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCertificatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCertificates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCertificatesResponse()
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


    def DescribeCountryAreaMapping(self, request):
        """本接口（DescribeCountryAreaMapping）用于获取国家地区编码映射表。

        :param request: 调用DescribeCountryAreaMapping所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeCountryAreaMappingRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeCountryAreaMappingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCountryAreaMapping", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCountryAreaMappingResponse()
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


    def DescribeDestRegions(self, request):
        """本接口（DescribeDestRegions）用于查询源站区域，即源站服务器所在区域。

        :param request: 调用DescribeDestRegions所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeDestRegionsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeDestRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDestRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDestRegionsResponse()
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


    def DescribeGroupAndStatisticsProxy(self, request):
        """该接口为内部接口，用于查询可以获取统计数据的通道组和通道信息

        :param request: 调用DescribeGroupAndStatisticsProxy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupAndStatisticsProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupAndStatisticsProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupAndStatisticsProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupAndStatisticsProxyResponse()
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


    def DescribeGroupDomainConfig(self, request):
        """本接口（DescribeGroupDomainConfig）用于获取通道组域名解析配置详情。

        :param request: 调用DescribeGroupDomainConfig所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupDomainConfigRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeGroupDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGroupDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGroupDomainConfigResponse()
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


    def DescribeHTTPListeners(self, request):
        """该接口（DescribeHTTPListeners）用来查询HTTP监听器信息。

        :param request: 调用DescribeHTTPListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHTTPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHTTPListenersResponse()
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


    def DescribeHTTPSListeners(self, request):
        """本接口（DescribeHTTPSListeners）用来查询HTTPS监听器信息。

        :param request: 调用DescribeHTTPSListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPSListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeHTTPSListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHTTPSListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHTTPSListenersResponse()
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


    def DescribeListenerRealServers(self, request):
        """该接口（DescribeListenerRealServers）用于查询TCP/UDP监听器源站列表，包括该监听器已经绑定的源站列表以及可以绑定的源站列表。

        :param request: 调用DescribeListenerRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListenerRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListenerRealServersResponse()
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


    def DescribeListenerStatistics(self, request):
        """该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300秒, 3600秒和86400秒的细粒度，取值为细粒度范围内最大值。

        :param request: 调用DescribeListenerStatistics所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeListenerStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeListenerStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeListenerStatisticsResponse()
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


    def DescribeProxies(self, request):
        """本接口（DescribeProxies）用于查询通道实例列表。

        :param request: 调用DescribeProxies所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxiesResponse()
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


    def DescribeProxiesStatus(self, request):
        """本接口（DescribeProxiesStatus）用于查询通道状态列表。

        :param request: 调用DescribeProxiesStatus所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesStatusRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxiesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxiesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxiesStatusResponse()
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


    def DescribeProxyAndStatisticsListeners(self, request):
        """该接口为内部接口，用于查询可以获取统计数据的通道和监听器信息

        :param request: 调用DescribeProxyAndStatisticsListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyAndStatisticsListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyAndStatisticsListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyAndStatisticsListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyAndStatisticsListenersResponse()
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


    def DescribeProxyDetail(self, request):
        """本接口（DescribeProxyDetail）用于查询通道详情。

        :param request: 调用DescribeProxyDetail所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyDetailRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyDetailResponse()
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


    def DescribeProxyGroupDetails(self, request):
        """本接口（DescribeProxyGroupDetails）用于查询通道组详情。

        :param request: 调用DescribeProxyGroupDetails所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyGroupDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyGroupDetailsResponse()
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


    def DescribeProxyGroupList(self, request):
        """本接口（DescribeProxyGroupList）用于拉取通道组列表及各通道组基本信息。

        :param request: 调用DescribeProxyGroupList所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupListRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyGroupListResponse()
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


    def DescribeProxyGroupStatistics(self, request):
        """该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。

        :param request: 调用DescribeProxyGroupStatistics所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyGroupStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyGroupStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyGroupStatisticsResponse()
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


    def DescribeProxyStatistics(self, request):
        """该接口用于查询监听器统计数据，包括出入带宽，出入包量，并发，丢包和时延数据。支持300, 3600和86400的细粒度，取值为细粒度范围内最大值。

        :param request: 调用DescribeProxyStatistics所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeProxyStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProxyStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProxyStatisticsResponse()
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


    def DescribeRealServerStatistics(self, request):
        """该接口（DescribeRealServerStatistics）用于查询源站健康检查结果的统计数据。源站状态展示位为1：正常或者0：异常。查询的源站需要在监听器或者规则上进行了绑定，查询时需指定绑定的监听器或者规则ID。该接口支持最近1，3，6，12，24小时内1分钟细粒度的源站状态统计数据展示。

        :param request: 调用DescribeRealServerStatistics所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServerStatisticsRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServerStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealServerStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealServerStatisticsResponse()
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


    def DescribeRealServers(self, request):
        """本接口（DescribeRealServers）用于查询源站信息，可以根据项目名查询所有的源站信息，此外支持指定IP机或者域名的源站模糊查询。

        :param request: 调用DescribeRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealServersResponse()
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


    def DescribeRealServersStatus(self, request):
        """本接口（DescribeRealServersStatus）用于查询源站是否已被规则或者监听器绑定

        :param request: 调用DescribeRealServersStatus所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersStatusRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRealServersStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRealServersStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRealServersStatusResponse()
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


    def DescribeRegionAndPrice(self, request):
        """该接口（DescribeRegionAndPrice）用于获取源站区域和带宽梯度价格

        :param request: 调用DescribeRegionAndPrice所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRegionAndPriceRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRegionAndPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegionAndPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionAndPriceResponse()
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


    def DescribeResourcesByTag(self, request):
        """本接口（DescribeResourcesByTag）用于根据标签来查询对应的资源信息，包括通道，通道组和源站。

        :param request: 调用DescribeResourcesByTag所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeResourcesByTagRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeResourcesByTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourcesByTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourcesByTagResponse()
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


    def DescribeRuleRealServers(self, request):
        """本接口（DescribeRuleRealServers）用于查询转发规则相关的源站信息， 包括该规则可绑定的源站信息和已绑定的源站信息。

        :param request: 调用DescribeRuleRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRuleRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRuleRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRuleRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuleRealServersResponse()
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


    def DescribeRules(self, request):
        """本接口（DescribeRules）用于查询监听器下的所有规则信息，包括规则域名，路径以及该规则下所绑定的源站列表。当通道版本为3.0时，该接口会返回该域名对应的高级认证配置信息。

        :param request: 调用DescribeRules所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRulesResponse()
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


    def DescribeSecurityPolicyDetail(self, request):
        """获取安全策略详情

        :param request: 调用DescribeSecurityPolicyDetail所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeSecurityPolicyDetailRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeSecurityPolicyDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityPolicyDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityPolicyDetailResponse()
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


    def DescribeTCPListeners(self, request):
        """该接口（DescribeTCPListeners）用于查询单通道或者通道组下的TCP监听器信息。

        :param request: 调用DescribeTCPListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeTCPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeTCPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTCPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTCPListenersResponse()
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


    def DescribeUDPListeners(self, request):
        """该接口（DescribeUDPListeners）用于查询单通道或者通道组下的UDP监听器信息

        :param request: 调用DescribeUDPListeners所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DescribeUDPListenersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DescribeUDPListenersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUDPListeners", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUDPListenersResponse()
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


    def DestroyProxies(self, request):
        """本接口（DestroyProxies）用于销毁。通道销毁后，不再产生任何费用。

        :param request: 调用DestroyProxies所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.DestroyProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.DestroyProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyProxiesResponse()
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


    def InquiryPriceCreateProxy(self, request):
        """本接口（InquiryPriceCreateProxy）用于创建加速通道询价。

        :param request: 调用InquiryPriceCreateProxy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.InquiryPriceCreateProxyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.InquiryPriceCreateProxyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateProxy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateProxyResponse()
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


    def ModifyCertificate(self, request):
        """本接口（ModifyCertificate）用于修改监听器下的域名对应的证书。该接口仅适用于version3.0的通道。

        :param request: 调用ModifyCertificate所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateResponse()
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


    def ModifyCertificateAttributes(self, request):
        """本接口（ModifyCertificateAttributes）用于修改证书，包括证明名字以及证书内容。

        :param request: 调用ModifyCertificateAttributes所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateAttributesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyCertificateAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCertificateAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCertificateAttributesResponse()
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


    def ModifyDomain(self, request):
        """本接口（ModifyDomain）用于监听器下的域名。当通道版本为3.0时，支持对该域名所对应的证书修改。

        :param request: 调用ModifyDomain所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyDomainRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyDomainResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDomain", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDomainResponse()
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


    def ModifyGroupDomainConfig(self, request):
        """本接口（ModifyGroupDomainConfig）用于配置通道组就近接入域名。

        :param request: 调用ModifyGroupDomainConfig所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyGroupDomainConfigRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyGroupDomainConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGroupDomainConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGroupDomainConfigResponse()
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


    def ModifyHTTPListenerAttribute(self, request):
        """该接口（ModifyHTTPListenerAttribute）用于修改通道的HTTP监听器配置信息，目前仅支持修改监听器的名称。
        注意：通道组通道暂时不支持HTTP/HTTPS监听器。

        :param request: 调用ModifyHTTPListenerAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHTTPListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHTTPListenerAttributeResponse()
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


    def ModifyHTTPSListenerAttribute(self, request):
        """该接口（ModifyHTTPSListenerAttribute）用于修改HTTPS监听器配置，当前不支持通道组和v1版本通道。

        :param request: 调用ModifyHTTPSListenerAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPSListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyHTTPSListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHTTPSListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHTTPSListenerAttributeResponse()
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


    def ModifyProxiesAttribute(self, request):
        """本接口（ModifyProxiesAttribute）用于修改实例的属性（目前只支持修改通道的名称）。

        :param request: 调用ModifyProxiesAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxiesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxiesAttributeResponse()
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


    def ModifyProxiesProject(self, request):
        """本接口（ModifyProxiesProject）用于修改通道所属项目。

        :param request: 调用ModifyProxiesProject所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesProjectRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxiesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxiesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxiesProjectResponse()
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


    def ModifyProxyConfiguration(self, request):
        """本接口（ModifyProxyConfiguration）用于修改通道的配置。根据当前业务的容量需求，扩容或缩容相关通道的配置。仅支持Scalarable为1的通道,Scalarable可通过接口DescribeProxies获取。

        :param request: 调用ModifyProxyConfiguration所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyConfigurationRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxyConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxyConfigurationResponse()
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


    def ModifyProxyGroupAttribute(self, request):
        """本接口（ModifyProxyGroupAttribute）用于修改通道组属性，目前仅支持修改通道组名称。

        :param request: 调用ModifyProxyGroupAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyGroupAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyProxyGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyProxyGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyProxyGroupAttributeResponse()
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


    def ModifyRealServerName(self, request):
        """本接口（ModifyRealServerName）用于修改源站的名称

        :param request: 调用ModifyRealServerName所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyRealServerNameRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyRealServerNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRealServerName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRealServerNameResponse()
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


    def ModifyRuleAttribute(self, request):
        """本接口（ModifyRuleAttribute）用于修改转发规则的信息，包括健康检查的配置以及转发策略。

        :param request: 调用ModifyRuleAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyRuleAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyRuleAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRuleAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRuleAttributeResponse()
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


    def ModifySecurityRule(self, request):
        """修改安全策略规则名

        :param request: 调用ModifySecurityRule所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifySecurityRuleRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifySecurityRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityRuleResponse()
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


    def ModifyTCPListenerAttribute(self, request):
        """本接口（ModifyTCPListenerAttribute）用于修改通道实例下TCP监听器配置，包括健康检查的配置，调度策略。

        :param request: 调用ModifyTCPListenerAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyTCPListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyTCPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTCPListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTCPListenerAttributeResponse()
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


    def ModifyUDPListenerAttribute(self, request):
        """本接口（ModifyUDPListenerAttribute）用于修改通道实例下UDP监听器配置，包括监听器名称和调度策略的修改。

        :param request: 调用ModifyUDPListenerAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.ModifyUDPListenerAttributeRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.ModifyUDPListenerAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyUDPListenerAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUDPListenerAttributeResponse()
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


    def OpenProxies(self, request):
        """该接口（OpenProxies）用于开启一条或者多条通道。

        :param request: 调用OpenProxies所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.OpenProxiesRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.OpenProxiesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenProxies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenProxiesResponse()
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


    def OpenSecurityPolicy(self, request):
        """开启安全策略

        :param request: 调用OpenSecurityPolicy所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.OpenSecurityPolicyRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.OpenSecurityPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenSecurityPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenSecurityPolicyResponse()
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


    def RemoveRealServers(self, request):
        """删除已添加的源站(服务器)IP或域名

        :param request: 调用RemoveRealServers所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.RemoveRealServersRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.RemoveRealServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveRealServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveRealServersResponse()
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


    def SetAuthentication(self, request):
        """本接口（SetAuthentication）用于通道的高级认证配置，包括认证方式选择，以及各种认证方式对应的证书选择。仅支持Version3.0的通道。

        :param request: 调用SetAuthentication所需参数的结构体。
        :type request: :class:`tencentcloud.gaap.v20180529.models.SetAuthenticationRequest`
        :rtype: :class:`tencentcloud.gaap.v20180529.models.SetAuthenticationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAuthentication", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAuthenticationResponse()
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