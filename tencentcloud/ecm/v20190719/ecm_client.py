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


    def AllocateAddresses(self, request):
        """申请一个或多个弹性公网IP（简称 EIP）

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateAddressesResponse()
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


    def AssignPrivateIpAddresses(self, request):
        """弹性网卡申请内网 IP

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignPrivateIpAddressesResponse()
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


    def AssociateAddress(self, request):
        """将弹性公网IP（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        将 EIP 绑定到主网卡的主内网IP上，绑定过程会把其上绑定的普通公网 IP 自动解绑并释放。
        将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。
        将 EIP 绑定到NAT网关，请使用接口EipBindNatGateway
        EIP 如果欠费或被封堵，则不能被绑定。
        只有状态为 UNBIND 的 EIP 才能够被绑定。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateAddressResponse()
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


    def AttachNetworkInterface(self, request):
        """弹性网卡绑定云主机

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachNetworkInterfaceResponse()
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


    def CreateImage(self, request):
        """本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。

        :param request: Request instance for CreateImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageResponse()
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


    def CreateNetworkInterface(self, request):
        """创建弹性网卡

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkInterfaceResponse()
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


    def CreateSecurityGroup(self, request):
        """创建安全组

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupResponse()
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


    def CreateSubnet(self, request):
        """创建子网，若创建成功，则此子网会成为此可用区的默认子网。

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetResponse()
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


    def CreateVpc(self, request):
        """创建私有网络

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcResponse()
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


    def DeleteNetworkInterface(self, request):
        """删除弹性网卡

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkInterfaceResponse()
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


    def DeleteSubnet(self, request):
        """删除子网，若子网为可用区下的默认子网，则默认子网会回退到系统自动创建的默认子网，非用户最新创建的子网。若默认子网不满足需求，可调用设置默认子网接口设置。

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSubnetResponse()
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


    def DeleteVpc(self, request):
        """删除私有网络

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DeleteVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcResponse()
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


    def DescribeAddressQuota(self, request):
        """查询您账户的弹性公网IP（简称 EIP）在当前地域的配额信息

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressQuotaResponse()
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


    def DescribeAddresses(self, request):
        """查询弹性公网IP列表

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressesResponse()
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


    def DescribeCustomImageTask(self, request):
        """查询导入镜像任务

        :param request: Request instance for DescribeCustomImageTask.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeCustomImageTaskRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeCustomImageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomImageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomImageTaskResponse()
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


    def DescribeDefaultSubnet(self, request):
        """查询可用区的默认子网

        :param request: Request instance for DescribeDefaultSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDefaultSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDefaultSubnetResponse()
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


    def DescribeImportImageOs(self, request):
        """查询外部导入镜像支持的OS列表

        :param request: Request instance for DescribeImportImageOs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeImportImageOsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeImportImageOsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImportImageOs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImportImageOsResponse()
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


    def DescribeInstanceVncUrl(self, request):
        """查询实例管理终端地址

        :param request: Request instance for DescribeInstanceVncUrl.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeInstanceVncUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceVncUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceVncUrlResponse()
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


    def DescribeNetworkInterfaces(self, request):
        """查询弹性网卡列表

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeNetworkInterfacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInterfaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInterfacesResponse()
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


    def DescribeSubnets(self, request):
        """查询子网列表

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetsResponse()
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


    def DescribeTaskResult(self, request):
        """查询EIP异步任务执行结果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultResponse()
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


    def DescribeTaskStatus(self, request):
        """本接口(DescribeTaskStatus)用于获取异步任务状态

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
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


    def DescribeVpcs(self, request):
        """查询私有网络列表

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcsResponse()
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


    def DetachNetworkInterface(self, request):
        """弹性网卡解绑云主机

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachNetworkInterfaceResponse()
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
            body = self.call("DisassociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateAddressResponse()
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


    def ImportCustomImage(self, request):
        """导入自定义镜像，支持 RAW、VHD、QCOW2、VMDK 镜像格式

        :param request: Request instance for ImportCustomImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ImportCustomImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImportCustomImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportCustomImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportCustomImageResponse()
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


    def ImportImage(self, request):
        """从CVM产品导入镜像到ECM

        :param request: Request instance for ImportImage.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ImportImageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportImage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportImageResponse()
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


    def MigrateNetworkInterface(self, request):
        """弹性网卡迁移

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigrateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigrateNetworkInterfaceResponse()
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
            body = self.call("MigratePrivateIpAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigratePrivateIpAddressResponse()
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


    def ModifyAddressAttribute(self, request):
        """修改弹性公网IP属性

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressAttributeResponse()
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


    def ModifyAddressesBandwidth(self, request):
        """调整弹性公网IP带宽

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressesBandwidthResponse()
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


    def ModifyDefaultSubnet(self, request):
        """修改在一个可用区下创建实例时使用的默认子网（创建实例时，未填写VPC参数时使用的sunbetId）

        :param request: Request instance for ModifyDefaultSubnet.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDefaultSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDefaultSubnetResponse()
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


    def ModifyImageAttribute(self, request):
        """本接口（ModifyImageAttribute）用于修改镜像属性。

        :param request: Request instance for ModifyImageAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyImageAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyImageAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageAttributeResponse()
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


    def ModifyModuleConfig(self, request):
        """修改模块配置，已关联实例的模块不支持调整配置。

        :param request: Request instance for ModifyModuleConfig.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleConfigRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyModuleConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyModuleConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyModuleConfigResponse()
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


    def ModifySubnetAttribute(self, request):
        """修改子网属性

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubnetAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubnetAttributeResponse()
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


    def ModifyVpcAttribute(self, request):
        """修改私有网络（VPC）的相关属性

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcAttributeResponse()
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
            body = self.call("ReleaseAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseAddressesResponse()
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


    def RemovePrivateIpAddresses(self, request):
        """弹性网卡退还内网 IP。
        退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。

        :param request: Request instance for RemovePrivateIpAddresses.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RemovePrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemovePrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemovePrivateIpAddressesResponse()
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


    def ResetInstancesPassword(self, request):
        """重置处于运行中状态的实例的密码，需要显式指定强制关机参数ForceStop。如果没有显式指定强制关机参数，则只有处于关机状态的实例才允许执行重置密码操作。

        :param request: Request instance for ResetInstancesPassword.
        :type request: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.ResetInstancesPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesPasswordResponse()
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


    def RunInstances(self, request):
        """创建ECM实例

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunInstancesResponse()
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


    def StartInstances(self, request):
        """只有状态为STOPPED的实例才可以进行此操作；接口调用成功时，实例会进入STARTING状态；启动实例成功时，实例会进入RUNNING状态。

        :param request: Request instance for StartInstances.
        :type request: :class:`tencentcloud.ecm.v20190719.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.ecm.v20190719.models.StartInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartInstancesResponse()
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
            body = self.call("StopInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopInstancesResponse()
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