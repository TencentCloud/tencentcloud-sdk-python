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
from tencentcloud.cvm.v20170312 import models


class CvmClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'cvm.tencentcloudapi.com'


    def AllocateHosts(self, request):
        """本接口 (AllocateHosts) 用于创建一个或多个指定配置的CDH实例。
        * 当HostChargeType为PREPAID时，必须指定HostChargePrepaid参数。

        :param request: 调用AllocateHosts所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.AllocateHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AllocateHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateHostsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateInstancesKeyPairs(self, request):
        """本接口 (AssociateInstancesKeyPairs) 用于将密钥绑定到实例上。

        * 将密钥的公钥写入到实例的`SSH`配置当中，用户就可以通过该密钥的私钥来登录实例。
        * 如果实例原来绑定过密钥，那么原来的密钥将失效。
        * 如果实例原来是通过密码登录，绑定密钥后无法使用密码登录。
        * 支持批量操作。每次请求批量实例的上限为100。如果批量实例存在不允许操作的实例，操作会以特定错误码返回。

        :param request: 调用AssociateInstancesKeyPairs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.AssociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.AssociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateInstancesKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateInstancesKeyPairsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDisasterRecoverGroup(self, request):
        """本接口 (CreateDisasterRecoverGroup)用于创建[分散置放群组](https://cloud.tencent.com/document/product/213/15486)。创建好的置放群组，可在[创建实例](https://cloud.tencent.com/document/api/213/15730)时指定。

        :param request: 调用CreateDisasterRecoverGroup所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateDisasterRecoverGroupRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateDisasterRecoverGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDisasterRecoverGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDisasterRecoverGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImage(self, request):
        """本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。

        :param request: 调用CreateImage所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateImageRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateImageResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateKeyPair(self, request):
        """本接口 (CreateKeyPair) 用于创建一个 `OpenSSH RSA` 密钥对，可以用于登录 `Linux` 实例。

        * 开发者只需指定密钥对名称，即可由系统自动创建密钥对，并返回所生成的密钥对的 `ID` 及其公钥、私钥的内容。
        * 密钥对名称不能和已经存在的密钥对的名称重复。
        * 私钥的内容可以保存到文件中作为 `SSH` 的一种认证方式。
        * 腾讯云不会保存用户的私钥，请妥善保管。

        :param request: 调用CreateKeyPair所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.CreateKeyPairRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.CreateKeyPairResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateKeyPair", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateKeyPairResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDisasterRecoverGroups(self, request):
        """本接口 (DeleteDisasterRecoverGroups)用于删除[分散置放群组](https://cloud.tencent.com/document/product/213/15486)。只有空的置放群组才能被删除，非空的群组需要先销毁组内所有云主机，才能执行删除操作，不然会产生删除置放群组失败的错误。

        :param request: 调用DeleteDisasterRecoverGroups所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDisasterRecoverGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDisasterRecoverGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteImages(self, request):
        """本接口（DeleteImages）用于删除一个或多个镜像。

        * 当[镜像状态](https://cloud.tencent.com/document/api/213/9452#image_state)为`创建中`和`使用中`时, 不允许删除。镜像状态可以通过[DescribeImages](https://cloud.tencent.com/document/api/213/9418)获取。
        * 每个地域最多只支持创建10个自定义镜像，删除镜像可以释放账户的配额。
        * 当镜像正在被其它账户分享时，不允许删除。

        :param request: 调用DeleteImages所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteKeyPairs(self, request):
        """本接口 (DeleteKeyPairs) 用于删除已在腾讯云托管的密钥对。

        * 可以同时删除多个密钥对。
        * 不能删除已被实例或镜像引用的密钥对，所以需要独立判断是否所有密钥对都被成功删除。

        :param request: 调用DeleteKeyPairs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DeleteKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DeleteKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteKeyPairsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDisasterRecoverGroupQuota(self, request):
        """本接口 (DescribeDisasterRecoverGroupQuota)用于查询[分散置放群组](https://cloud.tencent.com/document/product/213/15486)配额。

        :param request: 调用DescribeDisasterRecoverGroupQuota所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisasterRecoverGroupQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisasterRecoverGroupQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDisasterRecoverGroups(self, request):
        """本接口 (DescribeDisasterRecoverGroups)用于查询[分散置放群组](https://cloud.tencent.com/document/product/213/15486)信息。

        :param request: 调用DescribeDisasterRecoverGroups所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeDisasterRecoverGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDisasterRecoverGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDisasterRecoverGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHosts(self, request):
        """本接口 (DescribeHosts) 用于获取一个或多个CDH实例的详细信息。

        :param request: 调用DescribeHosts所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHostsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageQuota(self, request):
        """本接口(DescribeImageQuota)用于查询用户帐号的镜像配额。

        :param request: 调用DescribeImageQuota所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImageQuotaRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImageQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImageSharePermission(self, request):
        """本接口（DescribeImageSharePermission）用于查询镜像分享信息。

        :param request: 调用DescribeImageSharePermission所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImageSharePermissionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSharePermissionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImages(self, request):
        """本接口(DescribeImages) 用于查看镜像列表。

        * 可以通过指定镜像ID来查询指定镜像的详细信息，或通过设定过滤器来查询满足过滤条件的镜像的详细信息。
        * 指定偏移(Offset)和限制(Limit)来选择结果中的一部分，默认返回满足条件的前20个镜像信息。

        :param request: 调用DescribeImages所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeImportImageOs(self, request):
        """查看可以导入的镜像操作系统信息。

        :param request: 调用DescribeImportImageOs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeImportImageOsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeImportImageOsResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceFamilyConfigs(self, request):
        """本接口（DescribeInstanceFamilyConfigs）查询当前用户和地域所支持的机型族列表信息。

        :param request: 调用DescribeInstanceFamilyConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceFamilyConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceFamilyConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceFamilyConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceInternetBandwidthConfigs(self, request):
        """本接口 (DescribeInstanceInternetBandwidthConfigs) 用于查询实例带宽配置。

        * 只支持查询`BANDWIDTH_PREPAID`计费模式的带宽配置。
        * 接口返回实例的所有带宽配置信息（包含历史的带宽配置信息）。

        :param request: 调用DescribeInstanceInternetBandwidthConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceInternetBandwidthConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceInternetBandwidthConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceInternetBandwidthConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceInternetBandwidthConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceTypeConfigs(self, request):
        """本接口 (DescribeInstanceTypeConfigs) 用于查询实例机型配置。

        * 可以根据`zone`、`instance-family`来查询实例机型配置。过滤条件详见过滤器`Filter`。
        * 如果参数为空，返回指定地域的所有实例机型配置。

        :param request: 调用DescribeInstanceTypeConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceTypeConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceTypeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTypeConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceVncUrl(self, request):
        """本接口 ( DescribeInstanceVncUrl ) 用于查询实例管理终端地址。

        * 处于 `STOPPED` 状态的机器无法使用此功能。
        * 管理终端地址的有效期为 15 秒，调用接口成功后如果 15 秒内不使用该链接进行访问，管理终端地址自动失效，您需要重新查询。
        * 管理终端地址一旦被访问，将自动失效，您需要重新查询。
        * 如果连接断开，每分钟内重新连接的次数不能超过 30 次。
        * 获取到 `InstanceVncUrl` 后，您需要在在链接 <https://img.qcloud.com/qcloud/app/active_vnc/index.html?> 末尾加上参数 `InstanceVncUrl=xxxx`  。
          - 参数 `InstanceVncUrl` ：调用接口成功后会返回的 `InstanceVncUrl` 的值。

            最后组成的 URL 格式如下：

        ```
        https://img.qcloud.com/qcloud/app/active_vnc/index.html?InstanceVncUrl=wss%3A%2F%2Fbjvnc.qcloud.com%3A26789%2Fvnc%3Fs%3DaHpjWnRVMFNhYmxKdDM5MjRHNlVTSVQwajNUSW0wb2tBbmFtREFCTmFrcy8vUUNPMG0wSHZNOUUxRm5PMmUzWmFDcWlOdDJIbUJxSTZDL0RXcHZxYnZZMmRkWWZWcEZia2lyb09XMzdKNmM9
        ```

        :param request: 调用DescribeInstanceVncUrl所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceVncUrlRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstanceVncUrlResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstances(self, request):
        """本接口 (DescribeInstances) 用于查询一个或多个实例的详细信息。

        * 可以根据实例`ID`、实例名称或者实例计费模式等信息来查询实例的详细信息。过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的实例。

        :param request: 调用DescribeInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstancesStatus(self, request):
        """本接口 (DescribeInstancesStatus) 用于查询一个或多个实例的状态。

        * 可以根据实例`ID`来查询实例的状态。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的实例状态。

        :param request: 调用DescribeInstancesStatus所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesStatusRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInstancesStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInternetChargeTypeConfigs(self, request):
        """本接口（DescribeInternetChargeTypeConfigs）用于查询网络的计费类型。

        :param request: 调用DescribeInternetChargeTypeConfigs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeInternetChargeTypeConfigsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInternetChargeTypeConfigs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInternetChargeTypeConfigsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKeyPairs(self, request):
        """本接口 (DescribeKeyPairs) 用于查询密钥对信息。

        * 密钥对是通过一种算法生成的一对密钥，在生成的密钥对中，一个向外界公开，称为公钥；另一个用户自己保留，称为私钥。密钥对的公钥内容可以通过这个接口查询，但私钥内容系统不保留。

        :param request: 调用DescribeKeyPairs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKeyPairsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRegions(self, request):
        """本接口(DescribeRegions)用于查询地域信息。

        :param request: 调用DescribeRegions所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZoneInstanceConfigInfos(self, request):
        """本接口(DescribeZoneInstanceConfigInfos) 获取可用区的机型信息。

        :param request: 调用DescribeZoneInstanceConfigInfos所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeZoneInstanceConfigInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZoneInstanceConfigInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZoneInstanceConfigInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZones(self, request):
        """本接口(DescribeZones)用于查询可用区信息。

        :param request: 调用DescribeZones所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateInstancesKeyPairs(self, request):
        """本接口 (DisassociateInstancesKeyPairs) 用于解除实例的密钥绑定关系。

        * 只支持[`STOPPED`](https://cloud.tencent.com/document/api/213/9452#INSTANCE_STATE)状态的`Linux`操作系统的实例。
        * 解绑密钥后，实例可以通过原来设置的密码登录。
        * 如果原来没有设置密码，解绑后将无法使用 `SSH` 登录。可以调用 [ResetInstancesPassword](https://cloud.tencent.com/document/api/213/9397) 接口来设置登陆密码。
        * 支持批量操作。每次请求批量实例的上限为100。如果批量实例存在不允许操作的实例，操作会以特定错误码返回。

        :param request: 调用DisassociateInstancesKeyPairs所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.DisassociateInstancesKeyPairsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.DisassociateInstancesKeyPairsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateInstancesKeyPairs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateInstancesKeyPairsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportImage(self, request):
        """本接口(ImportImage)用于导入镜像，导入后的镜像可用于创建实例。

        :param request: 调用ImportImage所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ImportImageRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ImportImageResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ImportKeyPair(self, request):
        """本接口 (ImportKeyPair) 用于导入密钥对。

        * 本接口的功能是将密钥对导入到用户账户，并不会自动绑定到实例。如需绑定可以使用[AssociasteInstancesKeyPair](https://cloud.tencent.com/document/api/213/9404)接口。
        * 需指定密钥对名称以及该密钥对的公钥文本。
        * 如果用户只有私钥，可以通过 `SSL` 工具将私钥转换成公钥后再导入。

        :param request: 调用ImportKeyPair所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ImportKeyPairRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ImportKeyPairResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImportKeyPair", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImportKeyPairResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceModifyInstancesChargeType(self, request):
        """本接口 (InquiryPriceModifyInstancesChargeType) 用于切换实例的计费模式询价。

        * 只支持从 `POSTPAID_BY_HOUR` 计费模式切换为`PREPAID`计费模式。
        * 关机不收费的实例、`BC1`和`BS1`机型族的实例、设置定时销毁的实例不支持该操作。

        :param request: 调用InquiryPriceModifyInstancesChargeType所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceModifyInstancesChargeTypeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceModifyInstancesChargeTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceModifyInstancesChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceModifyInstancesChargeTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRenewInstances(self, request):
        """本接口 (InquiryPriceRenewInstances) 用于续费包年包月实例询价。

        * 只支持查询包年包月实例的续费价格。

        :param request: 调用InquiryPriceRenewInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRenewInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRenewInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResetInstance(self, request):
        """本接口 (InquiryPriceResetInstance) 用于重装实例询价。* 如果指定了`ImageId`参数，则使用指定的镜像进行重装询价；否则按照当前实例使用的镜像进行重装询价。* 目前只支持[系统盘类型](/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口实现`Linux`和`Windows`操作系统切换的重装询价。* 目前不支持海外地域的实例使用该接口实现`Linux`和`Windows`操作系统切换的重装询价。

        :param request: 调用InquiryPriceResetInstance所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResetInstancesInternetMaxBandwidth(self, request):
        """本接口 (InquiryPriceResetInstancesInternetMaxBandwidth) 用于调整实例公网带宽上限询价。

        * 不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/509)。
        * 对于`BANDWIDTH_PREPAID`计费方式的带宽，需要输入参数`StartTime`和`EndTime`，指定调整后的带宽的生效时间段。在这种场景下目前不支持调小带宽，会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。
        * 对于 `TRAFFIC_POSTPAID_BY_HOUR`、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽，使用该接口调整带宽上限是实时生效的，可以在带宽允许的范围内调大或者调小带宽，不支持输入参数 `StartTime` 和 `EndTime` 。
        * 接口不支持调整`BANDWIDTH_POSTPAID_BY_MONTH`计费方式的带宽。
        * 接口不支持批量调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽。
        * 接口不支持批量调整混合计费方式的带宽。例如不支持同时调整`TRAFFIC_POSTPAID_BY_HOUR`和`BANDWIDTH_PACKAGE`计费方式的带宽。

        :param request: 调用InquiryPriceResetInstancesInternetMaxBandwidth所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstancesInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstancesInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResetInstancesType(self, request):
        """本接口 (InquiryPriceResetInstancesType) 用于调整实例的机型询价。

        * 目前只支持[系统盘类型](https://cloud.tencent.com/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口进行调整机型询价。
        * 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口调整机型询价。
        * 目前不支持跨机型系统来调整机型，即使用该接口时指定的`InstanceType`和实例原来的机型需要属于同一系列。
        * 对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。

        :param request: 调用InquiryPriceResetInstancesType所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesTypeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResetInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetInstancesType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetInstancesTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResizeInstanceDisks(self, request):
        """本接口 (InquiryPriceResizeInstanceDisks) 用于扩容实例的数据盘询价。

        * 目前只支持扩容随实例购买的数据盘询价，且[数据盘类型](/document/api/213/9452#block_device)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。
        * 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口扩容数据盘询价。* 仅支持包年包月实例随机器购买的数据盘。* 目前只支持扩容一块数据盘询价。

        :param request: 调用InquiryPriceResizeInstanceDisks所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResizeInstanceDisksRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceResizeInstanceDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResizeInstanceDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResizeInstanceDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRunInstances(self, request):
        """本接口(InquiryPriceRunInstances)用于创建实例询价。本接口仅允许针对购买限制范围内的实例配置进行询价, 详见：[创建实例](https://cloud.tencent.com/document/api/213/15730)。

        :param request: 调用InquiryPriceRunInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRunInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.InquiryPriceRunInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRunInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRunInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDisasterRecoverGroupAttribute(self, request):
        """本接口 (ModifyDisasterRecoverGroupAttribute)用于修改[分散置放群组](https://cloud.tencent.com/document/product/213/15486)属性。

        :param request: 调用ModifyDisasterRecoverGroupAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyDisasterRecoverGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDisasterRecoverGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDisasterRecoverGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHostsAttribute(self, request):
        """本接口（ModifyHostsAttribute）用于修改CDH实例的属性，如实例名称和续费标记等。参数HostName和RenewFlag必须设置其中一个，但不能同时设置。

        :param request: 调用ModifyHostsAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyHostsAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyHostsAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHostsAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHostsAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyImageAttribute(self, request):
        """本接口（ModifyImageAttribute）用于修改镜像属性。

        * 已分享的镜像无法修改属性。

        :param request: 调用ModifyImageAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyImageAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyImageAttributeResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyImageSharePermission(self, request):
        """本接口（ModifyImageSharePermission）用于修改镜像分享信息。

        * 分享镜像后，被分享账户可以通过该镜像创建实例。
        * 每个自定义镜像最多可共享给50个账户。
        * 分享镜像无法更改名称，描述，仅可用于创建实例。
        * 只支持分享到对方账户相同地域。

        :param request: 调用ModifyImageSharePermission所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyImageSharePermissionRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyImageSharePermissionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageSharePermission", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageSharePermissionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstancesAttribute(self, request):
        """本接口 (ModifyInstancesAttribute) 用于修改实例的属性（目前只支持修改实例的名称）。

        * “实例名称”仅为方便用户自己管理之用，腾讯云并不以此名称作为提交工单或是进行实例管理操作的依据。
        * 支持批量操作。每次请求批量实例的上限为100。

        :param request: 调用ModifyInstancesAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesAttributeResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstancesChargeType(self, request):
        """本接口 (ModifyInstancesChargeType) 用于切换实例的计费模式。

        * 只支持从 `POSTPAID_BY_HOUR` 计费模式切换为`PREPAID`计费模式。
        * 关机不收费的实例、`BC1`和`BS1`机型族的实例、设置定时销毁的实例不支持该操作。

        :param request: 调用ModifyInstancesChargeType所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesChargeTypeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesChargeTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesChargeTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstancesProject(self, request):
        """本接口 (ModifyInstancesProject) 用于修改实例所属项目。

        * 项目为一个虚拟概念，用户可以在一个账户下面建立多个项目，每个项目中管理不同的资源；将多个不同实例分属到不同项目中，后续使用 [`DescribeInstances`](https://cloud.tencent.com/document/api/213/9388)接口查询实例，项目ID可用于过滤结果。
        * 绑定负载均衡的实例不支持修改实例所属项目，请先使用[`DeregisterInstancesFromLoadBalancer`](https://cloud.tencent.com/document/api/214/1258)接口解绑负载均衡。
        * 修改实例所属项目会自动解关联实例原来关联的安全组，修改完成后可能使用[`ModifySecurityGroupsOfInstance`](https://cloud.tencent.com/document/api/213/1367)接口关联安全组。
        * 支持批量操作。每次请求批量实例的上限为100。

        :param request: 调用ModifyInstancesProject所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesProjectRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyInstancesRenewFlag(self, request):
        """本接口 (ModifyInstancesRenewFlag) 用于修改包年包月实例续费标识。

        * 实例被标识为自动续费后，每次在实例到期时，会自动续费一个月。
        * 支持批量操作。每次请求批量实例的上限为100。

        :param request: 调用ModifyInstancesRenewFlag所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesRenewFlagRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyInstancesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyInstancesRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyInstancesRenewFlagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyKeyPairAttribute(self, request):
        """本接口 (ModifyKeyPairAttribute) 用于修改密钥对属性。

        * 修改密钥对ID所指定的密钥对的名称和描述信息。
        * 密钥对名称不能和已经存在的密钥对的名称重复。
        * 密钥对ID是密钥对的唯一标识，不可修改。

        :param request: 调用ModifyKeyPairAttribute所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ModifyKeyPairAttributeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ModifyKeyPairAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyKeyPairAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyKeyPairAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RebootInstances(self, request):
        """本接口 (RebootInstances) 用于重启实例。

        * 只有状态为`RUNNING`的实例才可以进行此操作。
        * 接口调用成功时，实例会进入`REBOOTING`状态；重启实例成功时，实例会进入`RUNNING`状态。
        * 支持强制重启。强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。
        * 支持批量操作，每次请求批量实例的上限为100。

        :param request: 调用RebootInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.RebootInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RebootInstancesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewHosts(self, request):
        """本接口 (RenewHosts) 用于续费包年包月CDH实例。

        * 只支持操作包年包月实例，否则操作会以特定[错误码](#4.-.E9.94.99.E8.AF.AF.E7.A0.81)返回。
        * 续费时请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。

        :param request: 调用RenewHosts所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.RenewHostsRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RenewHostsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewHosts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewHostsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewInstances(self, request):
        """本接口 (RenewInstances) 用于续费包年包月实例。

        * 只支持操作包年包月实例。
        * 续费时请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。

        :param request: 调用RenewInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.RenewInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RenewInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetInstance(self, request):
        """本接口 (ResetInstance) 用于重装指定实例上的操作系统。

        * 如果指定了`ImageId`参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装。
        * 系统盘将会被格式化，并重置；请确保系统盘中无重要文件。
        * `Linux`和`Windows`系统互相切换时，该实例系统盘`ID`将发生变化，系统盘关联快照将无法回滚、恢复数据。
        * 密码不指定将会通过站内信下发随机密码。
        * 目前只支持[系统盘类型](https://cloud.tencent.com/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口实现`Linux`和`Windows`操作系统切换。
        * 目前不支持海外地域的实例使用该接口实现`Linux`和`Windows`操作系统切换。

        :param request: 调用ResetInstance所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstanceRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetInstancesInternetMaxBandwidth(self, request):
        """本接口 (ResetInstancesInternetMaxBandwidth) 用于调整实例公网带宽上限。

        * 不同机型带宽上限范围不一致，具体限制详见[购买网络带宽](https://cloud.tencent.com/document/product/213/509)。
        * 对于 `BANDWIDTH_PREPAID` 计费方式的带宽，需要输入参数 `StartTime` 和 `EndTime` ，指定调整后的带宽的生效时间段。在这种场景下目前不支持调小带宽，会涉及扣费，请确保账户余额充足。可通过 [`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397) 接口查询账户余额。
        * 对于 `TRAFFIC_POSTPAID_BY_HOUR` 、 `BANDWIDTH_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽，使用该接口调整带宽上限是实时生效的，可以在带宽允许的范围内调大或者调小带宽，不支持输入参数 `StartTime` 和 `EndTime` 。
        * 接口不支持调整 `BANDWIDTH_POSTPAID_BY_MONTH` 计费方式的带宽。
        * 接口不支持批量调整 `BANDWIDTH_PREPAID` 和 `BANDWIDTH_POSTPAID_BY_HOUR` 计费方式的带宽。
        * 接口不支持批量调整混合计费方式的带宽。例如不支持同时调整 `TRAFFIC_POSTPAID_BY_HOUR` 和 `BANDWIDTH_PACKAGE` 计费方式的带宽。

        :param request: 调用ResetInstancesInternetMaxBandwidth所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetInstancesPassword(self, request):
        """本接口 (ResetInstancesPassword) 用于将实例操作系统的密码重置为用户指定的密码。

        * 只修改管理员帐号的密码。实例的操作系统不同，管理员帐号也会不一样(`Windows`为`Administrator`，`Ubuntu`为`ubuntu`，其它系统为`root`)。
        * 重置处于运行中状态的实例，需要显式指定强制关机参数`ForceStop`。如果没有显式指定强制关机参数，则只有处于关机状态的实例才允许执行重置密码操作。
        * 支持批量操作。将多个实例操作系统的密码重置为相同的密码。每次请求批量实例的上限为100。

        :param request: 调用ResetInstancesPassword所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesPasswordRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesPasswordResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetInstancesType(self, request):
        """本接口 (ResetInstancesType) 用于调整实例的机型。
        * 目前只支持[系统盘类型](/document/api/213/9452#block_device)是`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`类型的实例使用该接口进行机型调整。
        * 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口调整机型。* 目前不支持跨机型系统来调整机型，即使用该接口时指定的`InstanceType`和实例原来的机型需要属于同一系列。* 对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。

        :param request: 调用ResetInstancesType所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesTypeRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResetInstancesTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetInstancesType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetInstancesTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResizeInstanceDisks(self, request):
        """本接口 (ResizeInstanceDisks) 用于扩容实例的数据盘。

        * 目前只支持扩容随实例购买的数据盘，且[数据盘类型](/document/api/213/9452#block_device)为：`CLOUD_BASIC`、`CLOUD_PREMIUM`、`CLOUD_SSD`。* 目前不支持[CDH](https://cloud.tencent.com/document/product/416)实例使用该接口扩容数据盘。
        * 对于包年包月实例，使用该接口会涉及扣费，请确保账户余额充足。可通过[`DescribeAccountBalance`](https://cloud.tencent.com/document/product/378/4397)接口查询账户余额。
        * 目前只支持扩容一块数据盘。

        :param request: 调用ResizeInstanceDisks所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.ResizeInstanceDisksRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.ResizeInstanceDisksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResizeInstanceDisks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResizeInstanceDisksResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunInstances(self, request):
        """本接口 (RunInstances) 用于创建一个或多个指定配置的实例。

        * 实例创建成功后将自动开机启动，[实例状态](/document/api/213/9452#instance_state)变为“运行中”。
        * 预付费实例的购买会预先扣除本次实例购买所需金额，按小时后付费实例购买会预先冻结本次实例购买一小时内所需金额，在调用本接口前请确保账户余额充足。
        * 本接口允许购买的实例数量遵循[CVM实例购买限制](https://cloud.tencent.com/document/product/213/2664)，所创建的实例和官网入口创建的实例共用配额。
        * 本接口为异步接口，当创建请求下发成功后会返回一个实例`ID`列表，此时实例的创建并立即未完成。在此期间实例的状态将会处于“准备中”，可以通过调用 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口查询对应实例的状态，来判断创建有没有最终成功。如果实例的状态由“准备中”变为“运行中”，则为创建成功。

        :param request: 调用RunInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.RunInstancesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartInstances(self, request):
        """本接口 (StartInstances) 用于启动一个或多个实例。

        * 只有状态为`STOPPED`的实例才可以进行此操作。
        * 接口调用成功时，实例会进入`STARTING`状态；启动实例成功时，实例会进入`RUNNING`状态。
        * 支持批量操作。每次请求批量实例的上限为100。

        :param request: 调用StartInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.StartInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.StartInstancesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopInstances(self, request):
        """本接口 (StopInstances) 用于关闭一个或多个实例。

        * 只有状态为`RUNNING`的实例才可以进行此操作。
        * 接口调用成功时，实例会进入`STOPPING`状态；关闭实例成功时，实例会进入`STOPPED`状态。
        * 支持强制关闭。强制关机的效果等同于关闭物理计算机的电源开关。强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        * 支持批量操作。每次请求批量实例的上限为100。

        :param request: 调用StopInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.StopInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.StopInstancesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncImages(self, request):
        """本接口（SyncImages）用于将自定义镜像同步到其它地区。

        * 该接口每次调用只支持同步一个镜像。
        * 该接口支持多个同步地域。
        * 单个帐号在每个地域最多支持存在10个自定义镜像。

        :param request: 调用SyncImages所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.SyncImagesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.SyncImagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SyncImages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SyncImagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateInstances(self, request):
        """本接口 (TerminateInstances) 用于主动退还实例。

        * 不再使用的实例，可通过本接口主动退还。
        * 按量计费的实例通过本接口可直接退还；包年包月实例如符合[退还规则](https://cloud.tencent.com/document/product/213/9711)，也可通过本接口主动退还。
        * 支持批量操作，每次请求批量实例的上限为100。

        :param request: 调用TerminateInstances所需参数的结构体。
        :type request: :class:`tencentcloud.cvm.v20170312.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.cvm.v20170312.models.TerminateInstancesResponse`

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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)