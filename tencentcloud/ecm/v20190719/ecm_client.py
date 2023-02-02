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
from tencentcloud.ecm.v20190719 import models


class EcmClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'ecm.tencentcloudapi.com'
    _service = 'ecm'


    def AllocateAddresses(self, request):
        """申请一个或多个弹性公网IP（简称 EIP）

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6Addresses(self, request):
        """本接口（AssignIpv6Addresses）用于弹性网卡申请IPv6地址。

        :param request: Request instance for AssignIpv6Addresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignPrivateIpAddresses(self, request):
        """弹性网卡申请内网 IP

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.AssignPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateAddress(self, request):
        """将弹性公网IP（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        将 EIP 绑定到实例（ECM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        将 EIP 绑定到指定网卡的内网 IP上，内网IP已经绑定了EIP或普通公网IP，则反馈失败。必须先解绑该 EIP，才能再绑定新的。
        只有状态为 UNBIND 的 EIP 才能够绑定内网IP。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateSecurityGroups(self, request):
        """绑定安全组

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachDisks(self, request):
        """本接口（AttachDisks）用于挂载云硬盘。

        * 支持批量操作，将多块云盘挂载到同一云主机。如果多个云盘中存在不允许挂载的云盘，则操作不执行，返回特定的错误码。
        * 本接口为异步接口，当挂载云盘的请求成功返回时，表示后台已发起挂载云盘的操作，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态由“ATTACHING”变为“ATTACHED”，则为挂载成功。

        :param request: Request instance for AttachDisks.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AttachDisksRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AttachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachNetworkInterface(self, request):
        """弹性网卡绑定云主机

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.AttachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeregisterTargets(self, request):
        """批量解绑后端服务。

        :param request: Request instance for BatchDeregisterTargets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.BatchDeregisterTargetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.BatchDeregisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeregisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeregisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchModifyTargetWeight(self, request):
        """批量修改监听器绑定的后端机器的转发权重。

        :param request: Request instance for BatchModifyTargetWeight.
        :type request: :class:`tencentcloud.ecm.v20190719.models.BatchModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.BatchModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchRegisterTargets(self, request):
        """批量绑定后端目标。

        :param request: Request instance for BatchRegisterTargets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.BatchRegisterTargetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.BatchRegisterTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRegisterTargets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRegisterTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDisks(self, request):
        """本接口（CreateDisks）用于创建云硬盘。

        * 预付费云盘的购买会预先扣除本次云盘购买所需金额，在调用本接口前请确保账户余额充足。
        * 本接口支持传入数据盘快照来创建云盘，实现将快照数据复制到新购云盘上。
        * 本接口为异步接口，当创建请求下发成功后会返回一个新建的云盘ID列表，此时云盘的创建并未立即完成。可以通过调用[DescribeDisks](/document/product/362/16315)接口根据DiskId查询对应云盘，如果能查到云盘，且状态为'UNATTACHED'或'ATTACHED'，则表示创建成功。

        :param request: Request instance for CreateDisks.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateDisksRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHaVip(self, request):
        """本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateHaVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHaVip", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHaVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImage(self, request):
        """本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateKeyPair(self, request):
        """用于创建一个 OpenSSH RSA 密钥对，可以用于登录 Linux 实例。

        :param request: Request instance for CreateKeyPair.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateKeyPairRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKeyPair", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeyPairResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateListener(self, request):
        """创建负载均衡监听器。

        :param request: Request instance for CreateListener.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateListenerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateListener", params, headers=headers)
            response = json.loads(body)
            model = models.CreateListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLoadBalancer(self, request):
        """购买负载均衡实例。

        :param request: Request instance for CreateLoadBalancer.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateLoadBalancerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateModule(self, request):
        """创建模块

        :param request: Request instance for CreateModule.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateModuleRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateModuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkInterface(self, request):
        """创建弹性网卡

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRouteTable(self, request):
        """创建了VPC后，系统会创建一个默认路由表，所有新建的子网都会关联到默认路由表。默认情况下您可以直接使用默认路由表来管理您的路由策略。当您的路由策略较多时，您可以调用创建路由表接口创建更多路由表管理您的路由策略。

        :param request: Request instance for CreateRouteTable.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateRouteTableRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRoutes(self, request):
        """创建路由策略

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroup(self, request):
        """创建安全组

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroupPolicies(self, request):
        """<p>本接口（CreateSecurityGroupPolicies）用于创建安全组规则（SecurityGroupPolicy）。</p>
        <p>在 SecurityGroupPolicySet 参数中：</p>
        <ul>
        <li>Version 安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。</li>
        <li>在创建出站和入站规则（Egress 和 Ingress）时：<ul>
        <li>Protocol 字段支持输入TCP, UDP, ICMP, GRE, ALL。</li>
        <li>CidrBlock 字段允许输入符合cidr格式标准的任意字符串。在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        <li>SecurityGroupId 字段允许输入与待修改的安全组位于相同项目中的安全组 ID，包括这个安全组 ID 本身，代表安全组下所有云服务器的内网 IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个 ID 所关联的云服务器变化而变化，不需要重新修改。</li>
        <li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受，即 Protocol 字段不是 TCP 或 UDP 时，Protocol 和 Port 排他关系，不允许同时输入，否则会接口报错。</li>
        <li>Action 字段只允许输入 ACCEPT 或 DROP。</li>
        <li>CidrBlock, SecurityGroupId, AddressTemplate 是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。</li>
        <li>一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。</li>
        </ul></li></ul>
        <p>默认接口请求频率限制：20次/秒。</p>

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubnet(self, request):
        """创建子网，若创建成功，则此子网会成为此可用区的默认子网。

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpc(self, request):
        """创建私有网络

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateVpcResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteHaVip(self, request):
        """用于删除高可用虚拟IP（HAVIP）

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteHaVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHaVip", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHaVipResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DeleteImage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteListener(self, request):
        """删除负载均衡监听器。

        :param request: Request instance for DeleteListener.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteListenerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteListener", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLoadBalancer(self, request):
        """删除负载均衡实例。

        :param request: Request instance for DeleteLoadBalancer.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLoadBalancerListeners(self, request):
        """删除负载均衡多个监听器

        :param request: Request instance for DeleteLoadBalancerListeners.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerListenersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteLoadBalancerListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLoadBalancerListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLoadBalancerListenersResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DeleteModule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetworkInterface(self, request):
        """删除弹性网卡

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRouteTable(self, request):
        """删除路由表

        :param request: Request instance for DeleteRouteTable.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRoutes(self, request):
        """对某个路由表批量删除路由策略

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroup(self, request):
        """只有当前账号下的安全组允许被删除。
        安全组实例ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要先进行规则修改，再删除安全组。
        删除的安全组无法再找回，请谨慎调用。

        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroupPolicies(self, request):
        """SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSnapshots(self, request):
        """本接口（DeleteSnapshots）用于删除快照。

        * 快照必须处于NORMAL状态，快照状态可以通过[DescribeSnapshots](/document/product/362/15647)接口查询，见输出参数中SnapshotState字段解释。
        * 支持批量操作。如果多个快照存在无法删除的快照，则操作不执行，以返回特定的错误码返回。

        :param request: Request instance for DeleteSnapshots.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSnapshotsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSubnet(self, request):
        """删除子网，若子网为可用区下的默认子网，则默认子网会回退到系统自动创建的默认子网，非用户最新创建的子网。若默认子网不满足需求，可调用设置默认子网接口设置。

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpc(self, request):
        """删除私有网络

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressQuota(self, request):
        """查询您账户的弹性公网IP（简称 EIP）在当前地域的配额信息

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddresses(self, request):
        """查询弹性公网IP列表

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressesResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeBaseOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaseOverviewResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomImageTask(self, request):
        """查询导入镜像任务

        :param request: Request instance for DescribeCustomImageTask.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeCustomImageTaskRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeCustomImageTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomImageTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomImageTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDefaultSubnet(self, request):
        """查询可用区的默认子网

        :param request: Request instance for DescribeDefaultSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDisks(self, request):
        """本接口（DescribeDisks）用于查询云硬盘列表。

        * 可以根据云硬盘ID、云硬盘类型或者云硬盘状态等信息来查询云硬盘的详细信息，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的云硬盘列表。

        :param request: Request instance for DescribeDisks.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeDisksRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHaVips(self, request):
        """用于查询高可用虚拟IP（HAVIP）列表。

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeHaVipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHaVips", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHaVipsResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeImage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImportImageOs(self, request):
        """查询外部导入镜像支持的OS列表

        :param request: Request instance for DescribeImportImageOs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeImportImageOsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeImportImageOsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImportImageOs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImportImageOsResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeInstanceTypeConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTypeConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceVncUrl(self, request):
        """查询实例管理终端地址

        :param request: Request instance for DescribeInstanceVncUrl.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceVncUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceVncUrlResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeInstancesDeniedActions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDeniedActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeListeners(self, request):
        """查询负载均衡的监听器列表。

        :param request: Request instance for DescribeListeners.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeListenersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeListenersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeListeners", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeListenersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoadBalanceTaskStatus(self, request):
        """查询负载均衡相关的任务状态

        :param request: Request instance for DescribeLoadBalanceTaskStatus.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalanceTaskStatusRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalanceTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalanceTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalanceTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLoadBalancers(self, request):
        """查询负载均衡实例列表。

        :param request: Request instance for DescribeLoadBalancers.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalancersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeLoadBalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLoadBalancers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLoadBalancersResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeModule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModuleResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeModuleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModuleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMonthPeakNetwork(self, request):
        """获取客户节点上的出入带宽月峰和计费带宽信息

        :param request: Request instance for DescribeMonthPeakNetwork.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeMonthPeakNetworkRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeMonthPeakNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonthPeakNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonthPeakNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkInterfaces(self, request):
        """查询弹性网卡列表

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkInterfacesResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribeNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePackingQuotaGroup(self, request):
        """使用本接口获取某种机型在某些区域的装箱配额（当使用虚拟机型时，返回的是一组相互关联的装箱配额）。

        :param request: Request instance for DescribePackingQuotaGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePackingQuotaGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePackingQuotaGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePackingQuotaGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePackingQuotaGroupResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribePeakBaseOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakBaseOverviewResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("DescribePeakNetworkOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePeakNetworkOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePriceRunInstance(self, request):
        """查询实例价格

        :param request: Request instance for DescribePriceRunInstance.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribePriceRunInstanceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribePriceRunInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePriceRunInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePriceRunInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRouteConflicts(self, request):
        """查询自定义路由策略与云联网路由策略冲突列表

        :param request: Request instance for DescribeRouteConflicts.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteConflictsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteConflictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteConflicts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteConflictsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRouteTables(self, request):
        """查询路由表对象列表

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeRouteTablesResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupAssociationStatistics(self, request):
        """查询安全组关联实例统计

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupAssociationStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupAssociationStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupAssociationStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupLimits(self, request):
        """查询用户安全组配额

        :param request: Request instance for DescribeSecurityGroupLimits.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupLimitsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupPolicies(self, request):
        """查询安全组规则

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroups(self, request):
        """查看安全组

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSnapshots(self, request):
        """本接口（DescribeSnapshots）用于查询快照的详细信息。

        * 根据快照ID、创建快照的云硬盘ID、创建快照的云硬盘类型等对结果进行过滤，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        *  如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的快照列表。

        :param request: Request instance for DescribeSnapshots.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSnapshotsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSnapshotsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshots", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubnets(self, request):
        """查询子网列表

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargetHealth(self, request):
        """获取负载均衡后端服务的健康检查状态。

        :param request: Request instance for DescribeTargetHealth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetHealthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetHealthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargetHealth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetHealthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTargets(self, request):
        """查询负载均衡绑定的后端服务列表。

        :param request: Request instance for DescribeTargets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTargetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTargets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTargetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResult(self, request):
        """查询EIP异步任务执行结果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskStatus(self, request):
        """本接口(DescribeTaskStatus)用于获取异步任务状态

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskStatusResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcs(self, request):
        """查询私有网络列表

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def DetachDisks(self, request):
        """本接口（DetachDisks）用于卸载云硬盘。

        * 支持批量操作，卸载挂载在同一主机上的多块云盘。如果多块云盘中存在不允许卸载的云盘，则操作不执行，返回特定的错误码。
        * 本接口为异步接口，当请求成功返回时，云盘并未立即从主机卸载，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态由“ATTACHED”变为“UNATTACHED”，则为卸载成功。

        :param request: Request instance for DetachDisks.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DetachDisksRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DetachDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachDisks", params, headers=headers)
            response = json.loads(body)
            model = models.DetachDisksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachNetworkInterface(self, request):
        """弹性网卡解绑云主机

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DetachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableRoutes(self, request):
        """禁用已启用的子网路由

        :param request: Request instance for DisableRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisableRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisableRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateAddress(self, request):
        """解绑弹性公网IP（简称 EIP）
        只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。
        EIP 如果被封堵，则不能进行解绑定操作。

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateInstancesKeyPairs(self, request):
        """用于解除实例的密钥绑定关系。

        :param request: Request instance for DisassociateInstancesKeyPairs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateInstancesKeyPairs", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateInstancesKeyPairsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateSecurityGroups(self, request):
        """解绑安全组

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableRoutes(self, request):
        """启用已禁用的子网路由。
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。

        :param request: Request instance for EnableRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.EnableRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.EnableRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.EnableRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportCustomImage(self, request):
        """导入自定义镜像，支持 RAW、VHD、QCOW2、VMDK 镜像格式

        :param request: Request instance for ImportCustomImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ImportCustomImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImportCustomImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportCustomImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImportCustomImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportImage(self, request):
        """从CVM产品导入镜像到ECM

        :param request: Request instance for ImportImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportImage", params, headers=headers)
            response = json.loads(body)
            model = models.ImportImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigrateNetworkInterface(self, request):
        """弹性网卡迁移

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigratePrivateIpAddress(self, request):
        """弹性网卡内网IP迁移。
        该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。
        迁移前后的弹性网卡必须在同一个子网内。

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigratePrivateIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigratePrivateIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.MigratePrivateIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressAttribute(self, request):
        """修改弹性公网IP属性

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressesBandwidth(self, request):
        """调整弹性公网IP带宽

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDefaultSubnet(self, request):
        """修改在一个可用区下创建实例时使用的默认子网（创建实例时，未填写VPC参数时使用的sunbetId）

        :param request: Request instance for ModifyDefaultSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDefaultSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDefaultSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHaVipAttribute(self, request):
        """用于修改高可用虚拟IP（HAVIP）属性

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyHaVipAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHaVipAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHaVipAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyImageAttribute(self, request):
        """本接口（ModifyImageAttribute）用于修改镜像属性。

        :param request: Request instance for ModifyImageAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyImageAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyImageAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyImageAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyImageAttributeResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ModifyInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIpv6AddressesAttribute(self, request):
        """本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡IPv6地址属性。

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyIpv6AddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIpv6AddressesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIpv6AddressesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyListener(self, request):
        """修改负载均衡监听器属性。

        :param request: Request instance for ModifyListener.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyListenerRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyListener", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLoadBalancerAttributes(self, request):
        """修改负载均衡实例的属性。

        :param request: Request instance for ModifyLoadBalancerAttributes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyLoadBalancerAttributesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyLoadBalancerAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLoadBalancerAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLoadBalancerAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModuleConfig(self, request):
        """修改模块配置，已关联实例的模块不支持调整配置。

        :param request: Request instance for ModifyModuleConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModuleDisableWanIp(self, request):
        """修改模块是否禁止分配外网ip的属性。

        :param request: Request instance for ModifyModuleDisableWanIp.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleDisableWanIpRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleDisableWanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleDisableWanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleDisableWanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModuleImage(self, request):
        """修改模块的默认镜像

        :param request: Request instance for ModifyModuleImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleImage", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModuleIpDirect(self, request):
        """修改模块IP直通。

        :param request: Request instance for ModifyModuleIpDirect.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleIpDirectRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleIpDirectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleIpDirect", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleIpDirectResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ModifyModuleName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleNameResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ModifyModuleNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyModuleSecurityGroups(self, request):
        """修改模块默认安全组

        :param request: Request instance for ModifyModuleSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyModuleSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyModuleSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrivateIpAddressesAttribute(self, request):
        """用于修改弹性网卡内网IP属性。

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyPrivateIpAddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateIpAddressesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateIpAddressesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRouteTableAttribute(self, request):
        """修改路由表属性

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRouteTableAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRouteTableAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupAttribute(self, request):
        """修改安全组属性

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupPolicies(self, request):
        """修改安全组出站和入站规则

        :param request: Request instance for ModifySecurityGroupPolicies.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubnetAttribute(self, request):
        """修改子网属性

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetPort(self, request):
        """修改监听器绑定的后端机器的端口。

        :param request: Request instance for ModifyTargetPort.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetPortRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTargetWeight(self, request):
        """修改监听器绑定的后端机器的转发权重。

        :param request: Request instance for ModifyTargetWeight.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetWeightRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyTargetWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTargetWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTargetWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpcAttribute(self, request):
        """修改私有网络（VPC）的相关属性

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeResponse`

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
                raise TencentCloudSDKException(e.message, e.message)


    def RebootInstances(self, request):
        """只有状态为RUNNING的实例才可以进行此操作；接口调用成功时，实例会进入REBOOTING状态；重启实例成功时，实例会进入RUNNING状态；支持强制重启，强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。

        :param request: Request instance for RebootInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RebootInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebootInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RebootInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseAddresses(self, request):
        """释放一个或多个弹性公网IP（简称 EIP）。
        该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。
        只有状态为 UNBIND 的 EIP 才能进行释放操作。

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReleaseAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseIpv6Addresses(self, request):
        """本接口（UnassignIpv6Addresses）用于释放弹性网卡IPv6地址。

        :param request: Request instance for ReleaseIpv6Addresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReleaseIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReleaseIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemovePrivateIpAddresses(self, request):
        """弹性网卡退还内网 IP。
        退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。

        :param request: Request instance for RemovePrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemovePrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.RemovePrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRouteTableAssociation(self, request):
        """修改子网关联的路由表，一个子网只能关联一个路由表。

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReplaceRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceRouteTableAssociation", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceRouteTableAssociationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRoutes(self, request):
        """替换路由策略

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReplaceRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceSecurityGroupPolicy(self, request):
        """替换单条安全组路由规则, 单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ReplaceSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceSecurityGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceSecurityGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ResetInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ResetInstancesMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetInstancesPassword(self, request):
        """重置处于运行中状态的实例的密码，需要显式指定强制关机参数ForceStop。如果没有显式指定强制关机参数，则只有处于关机状态的实例才允许执行重置密码操作。

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetInstancesPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetInstancesPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetRoutes(self, request):
        """对某个路由表名称和所有路由策略（Route）进行重新设置

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ResetRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunInstances(self, request):
        """创建ECM实例。

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetLoadBalancerSecurityGroups(self, request):
        """设置负载均衡实例的安全组。

        :param request: Request instance for SetLoadBalancerSecurityGroups.
        :type request: :class:`tencentcloud.ecm.v20190719.models.SetLoadBalancerSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SetLoadBalancerSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetLoadBalancerSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.SetLoadBalancerSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetSecurityGroupForLoadbalancers(self, request):
        """绑定或解绑一个安全组到多个负载均衡实例。

        :param request: Request instance for SetSecurityGroupForLoadbalancers.
        :type request: :class:`tencentcloud.ecm.v20190719.models.SetSecurityGroupForLoadbalancersRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.SetSecurityGroupForLoadbalancersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetSecurityGroupForLoadbalancers", params, headers=headers)
            response = json.loads(body)
            model = models.SetSecurityGroupForLoadbalancersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartInstances(self, request):
        """只有状态为STOPPED的实例才可以进行此操作；接口调用成功时，实例会进入STARTING状态；启动实例成功时，实例会进入RUNNING状态。

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopInstances(self, request):
        """只有处于"RUNNING"状态的实例才能够进行关机操作；
        调用成功时，实例会进入STOPPING状态；关闭实例成功时，实例会进入STOPPED状态；
        支持强制关闭，强制关机的效果等同于关闭物理计算机的电源开关，强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。

        :param request: Request instance for StopInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StopInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstances", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateDisks(self, request):
        """本接口（TerminateDisks）用于退还云硬盘。

        * 不再使用的云盘，可通过本接口主动退还。
        * 本接口支持退还预付费云盘和按小时后付费云盘。按小时后付费云盘可直接退还，预付费云盘需符合退还规则。
        * 支持批量操作，每次请求批量云硬盘的上限为50。如果批量云盘存在不允许操作的，请求会以特定错误码返回。

        :param request: Request instance for TerminateDisks.
        :type request: :class:`tencentcloud.ecm.v20190719.models.TerminateDisksRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.TerminateDisksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDisks", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDisksResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)