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
from tencentcloud.bmvpc.v20180625 import models


class BmvpcClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmvpc.tencentcloudapi.com'
    _service = 'bmvpc'


    def AcceptVpcPeerConnection(self, request):
        """接受黑石对等连接

        :param request: Request instance for AcceptVpcPeerConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.AcceptVpcPeerConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.AcceptVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptVpcPeerConnection", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptVpcPeerConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AsyncRegisterIps(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        批量注册虚拟IP，异步接口。通过接口来查询任务进度。每次请求最多注册256个IP

        :param request: Request instance for AsyncRegisterIps.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.AsyncRegisterIpsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.AsyncRegisterIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AsyncRegisterIps", params, headers=headers)
            response = json.loads(body)
            model = models.AsyncRegisterIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindEipsToNatGateway(self, request):
        """NAT网关绑定EIP接口，可将EIP绑定到NAT网关，该EIP作为访问外网的源IP地址，将流量发送到Internet

        :param request: Request instance for BindEipsToNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.BindEipsToNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.BindEipsToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindEipsToNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.BindEipsToNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindIpsToNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        可用于将子网的部分IP绑定到NAT网关

        :param request: Request instance for BindIpsToNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.BindIpsToNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.BindIpsToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindIpsToNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.BindIpsToNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindSubnetsToNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        NAT网关绑定子网后，该子网内全部IP可出公网

        :param request: Request instance for BindSubnetsToNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.BindSubnetsToNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.BindSubnetsToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindSubnetsToNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.BindSubnetsToNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomerGateway(self, request):
        """90天无调用

        本接口（CreateCustomerGateway）用于创建对端网关。

        :param request: Request instance for CreateCustomerGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomerGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomerGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDockerSubnetWithVlan(self, request):
        """创建黑石Docker子网， 如果不指定VlanId，将会分配2000--2999范围的VlanId; 子网会关闭分布式网关

        :param request: Request instance for CreateDockerSubnetWithVlan.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateDockerSubnetWithVlanRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateDockerSubnetWithVlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDockerSubnetWithVlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDockerSubnetWithVlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHostedInterface(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        本接口（CreateHostedInterface）用于黑石托管机器加入带VLANID不为5的子网。

        1) 不能加入vlanId 为5的子网，只能加入VLANID范围为2000-2999的子网。
        2) 每台托管机器最多可以加入20个子网。
        3) 每次调用最多能支持传入10台托管机器。

        :param request: Request instance for CreateHostedInterface.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateHostedInterfaceRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateHostedInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHostedInterface", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHostedInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInterfaces(self, request):
        """物理机加入子网

        :param request: Request instance for CreateInterfaces.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateInterfacesRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        创建NAT网关接口，可针对网段方式、子网全部IP、子网部分IP这三种方式创建NAT网关

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoutePolicies(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        创建黑石路由表的路由规则

        :param request: Request instance for CreateRoutePolicies.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateRoutePoliciesRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateRoutePoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoutePolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoutePoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubnet(self, request):
        """创建黑石私有网络的子网
        访问管理: 用户可以对VpcId进行授权操作。例如设置资源为["qcs::bmvpc:::unVpc/vpc-xxxxx"]

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVirtualSubnetWithVlan(self, request):
        """创建黑石虚拟子网， 虚拟子网用于在黑石上创建虚拟网络，与黑石子网要做好规划。虚拟子网会分配2000-2999的VlanId。

        :param request: Request instance for CreateVirtualSubnetWithVlan.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateVirtualSubnetWithVlanRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateVirtualSubnetWithVlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVirtualSubnetWithVlan", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVirtualSubnetWithVlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpc(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        创建黑石私有网络

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcPeerConnection(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        创建对等连接

        :param request: Request instance for CreateVpcPeerConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.CreateVpcPeerConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.CreateVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcPeerConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcPeerConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomerGateway(self, request):
        """本接口（DeleteCustomerGateway）用于删除对端网关。

        :param request: Request instance for DeleteCustomerGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomerGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomerGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHostedInterface(self, request):
        """本接口用于托管机器从VLANID不为5的子网中移除。
        1) 不能从vlanId 为5的子网中移除。
        2) 每次调用最多能支持传入10台物理机。

        :param request: Request instance for DeleteHostedInterface.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteHostedInterfaceRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteHostedInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHostedInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHostedInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHostedInterfaces(self, request):
        """托管机器移除子网批量接口，传入一台托管机器和多个子网，批量移除这些子网。异步接口，接口返回TaskId。

        :param request: Request instance for DeleteHostedInterfaces.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteHostedInterfacesRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteHostedInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHostedInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHostedInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInterfaces(self, request):
        """物理机移除子网批量接口，传入一台物理机和多个子网，批量移除这些子网。异步接口，接口返回TaskId。

        :param request: Request instance for DeleteInterfaces.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteInterfacesRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        删除NAT网关

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoutePolicy(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        删除黑石路由表路由规则

        :param request: Request instance for DeleteRoutePolicy.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteRoutePolicyRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteRoutePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoutePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoutePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubnet(self, request):
        """本接口（DeleteSubnet）用于删除黑石私有网络子网。
        删除子网前，请清理该子网下所有资源，包括物理机、负载均衡、黑石数据库、弹性IP、NAT网关等资源

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVirtualIp(self, request):
        """退还虚拟IP。此接口只能退还虚拟IP，物理机IP不能退还。

        :param request: Request instance for DeleteVirtualIp.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVirtualIpRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVirtualIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVirtualIp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVirtualIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpc(self, request):
        """本接口(DeleteVpc)用于删除黑石私有网络(VPC)。

        删除私有网络前，请清理该私有网络下所有资源，包括子网、负载均衡、弹性 IP、对等连接、NAT 网关、专线通道、SSLVPN 等资源。

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcPeerConnection(self, request):
        """删除黑石对等连接

        :param request: Request instance for DeleteVpcPeerConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpcPeerConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcPeerConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcPeerConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnConnection(self, request):
        """本接口(DeleteVpnConnection)用于删除VPN通道。

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpnConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGateway(self, request):
        """本接口（DeleteVpnGateway）用于删除VPN网关。

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpnGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeleteVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeregisterIps(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        注销私有网络IP为空闲

        :param request: Request instance for DeregisterIps.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DeregisterIpsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DeregisterIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeregisterIps", params, headers=headers)
            response = json.loads(body)
            model = models.DeregisterIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerGateways(self, request):
        """本接口（DescribeCustomerGateways）用于查询对端网关列表。

        :param request: Request instance for DescribeCustomerGateways.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeCustomerGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGateways(self, request):
        """获取NAT网关信息，包括NAT网关 ID、网关名称、私有网络、网关并发连接上限、绑定EIP列表等

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeNatGatewaysRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatSubnets(self, request):
        """可获取NAT网关绑定的子网信息

        :param request: Request instance for DescribeNatSubnets.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeNatSubnetsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeNatSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoutePolicies(self, request):
        """本接口（DescribeRoutePolicies）用于查询路由表条目。

        :param request: Request instance for DescribeRoutePolicies.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeRoutePoliciesRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeRoutePoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoutePolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoutePoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTables(self, request):
        """本接口（DescribeRouteTables）用于查询路由表。

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetAvailableIps(self, request):
        """获取子网内可用IP列表

        :param request: Request instance for DescribeSubnetAvailableIps.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetAvailableIpsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetAvailableIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetAvailableIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetAvailableIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetByDevice(self, request):
        """物理机可以加入物理机子网，虚拟子网，DOCKER子网，通过此接口可以查询物理机加入的子网。

        :param request: Request instance for DescribeSubnetByDevice.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetByDeviceRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetByDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetByDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetByDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetByHostedDevice(self, request):
        """托管可以加入物理机子网，虚拟子网，DOCKER子网，通过此接口可以查询托管加入的子网。

        :param request: Request instance for DescribeSubnetByHostedDevice.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetByHostedDeviceRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetByHostedDeviceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetByHostedDevice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetByHostedDeviceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnets(self, request):
        """本接口（DescribeSubnets）用于查询黑石子网列表。

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """根据任务ID，获取任务的执行状态

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcPeerConnections(self, request):
        """获取对等连接列表

        :param request: Request instance for DescribeVpcPeerConnections.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcPeerConnectionsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcPeerConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcPeerConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcPeerConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcQuota(self, request):
        """本接口（DescribeVpcQuota）用于查询用户VPC相关配额限制。

        :param request: Request instance for DescribeVpcQuota.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcQuotaRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcResource(self, request):
        """查询黑石私有网络关联资源

        :param request: Request instance for DescribeVpcResource.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcResourceRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcView(self, request):
        """本接口（DescribeVpcView）用于查询VPC网络拓扑视图。

        :param request: Request instance for DescribeVpcView.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcViewRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcViewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcView", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcViewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcs(self, request):
        """本接口（DescribeVpcs）用于查询私有网络列表。
        本接口不传参数时，返回默认排序下的前20条VPC信息。

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnConnections(self, request):
        """本接口（DescribeVpnConnections）查询VPN通道列表。

        :param request: Request instance for DescribeVpnConnections.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpnConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGateways(self, request):
        """本接口（DescribeVpnGateways）用于查询VPN网关列表。

        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DescribeVpnGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadCustomerGatewayConfiguration(self, request):
        """90天无调用

        本接口(DownloadCustomerGatewayConfiguration)用于下载VPN通道配置。

        :param request: Request instance for DownloadCustomerGatewayConfiguration.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.DownloadCustomerGatewayConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadCustomerGatewayConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadCustomerGatewayConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomerGatewayAttribute(self, request):
        """本接口（ModifyCustomerGatewayAttribute）用于修改对端网关信息。

        :param request: Request instance for ModifyCustomerGatewayAttribute.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyCustomerGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomerGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomerGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoutePolicy(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        修改自定义路由

        :param request: Request instance for ModifyRoutePolicy.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyRoutePolicyRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyRoutePolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoutePolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoutePolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRouteTable(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        修改路由表

        :param request: Request instance for ModifyRouteTable.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyRouteTableRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubnetAttribute(self, request):
        """修改子网属性

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubnetAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubnetAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubnetDHCPRelay(self, request):
        """修改子网DHCP Relay属性

        :param request: Request instance for ModifySubnetDHCPRelay.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifySubnetDHCPRelayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifySubnetDHCPRelayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubnetDHCPRelay", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubnetDHCPRelayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAttribute(self, request):
        """本接口（ModifyVpcAttribute）用于修改VPC的标识名称和控制VPC的监控起停。

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcPeerConnection(self, request):
        """修改黑石对等连接

        :param request: Request instance for ModifyVpcPeerConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpcPeerConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcPeerConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcPeerConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnConnectionAttribute(self, request):
        """本接口（ModifyVpnConnectionAttribute）用于修改VPN通道。

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpnConnectionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnConnectionAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnConnectionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayAttribute(self, request):
        """本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。

        :param request: Request instance for ModifyVpnGatewayAttribute.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ModifyVpnGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectVpcPeerConnection(self, request):
        """拒绝黑石对等连接申请

        :param request: Request instance for RejectVpcPeerConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.RejectVpcPeerConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.RejectVpcPeerConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectVpcPeerConnection", params, headers=headers)
            response = json.loads(body)
            model = models.RejectVpcPeerConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetVpnConnection(self, request):
        """本接口(ResetVpnConnection)用于重置VPN通道。

        :param request: Request instance for ResetVpnConnection.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.ResetVpnConnectionRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.ResetVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ResetVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindEipsFromNatGateway(self, request):
        """NAT网关解绑该EIP后，NAT网关将不会使用该EIP作为访问外网的源IP地址

        :param request: Request instance for UnbindEipsFromNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.UnbindEipsFromNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.UnbindEipsFromNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindEipsFromNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindEipsFromNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindIpsFromNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        NAT网关解绑IP接口，可将子网的部分IP从NAT网关中解绑

        :param request: Request instance for UnbindIpsFromNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.UnbindIpsFromNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.UnbindIpsFromNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindIpsFromNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindIpsFromNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindSubnetsFromNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        NAT网关解绑子网接口，可将子网解绑NAT网关

        :param request: Request instance for UnbindSubnetsFromNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.UnbindSubnetsFromNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.UnbindSubnetsFromNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindSubnetsFromNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindSubnetsFromNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeNatGateway(self, request):
        """黑石1.0接口，业务已下线，90天无调用

        升级NAT网关接口，可NAT网关修改为小型NAT网关、中型NAT网关、以及大型NAT网关

        :param request: Request instance for UpgradeNatGateway.
        :type request: :class:`tencentcloud.bmvpc.v20180625.models.UpgradeNatGatewayRequest`
        :rtype: :class:`tencentcloud.bmvpc.v20180625.models.UpgradeNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))