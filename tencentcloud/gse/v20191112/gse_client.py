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
from tencentcloud.gse.v20191112 import models


class GseClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'gse.tencentcloudapi.com'
    _service = 'gse'


    def AttachCcnInstances(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（AttachCcnInstances）用于关联云联网实例。

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyFleet(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CopyFleet）用于复制服务器舰队。

        :param request: Request instance for CopyFleet.
        :type request: :class:`tencentcloud.gse.v20191112.models.CopyFleetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CopyFleetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyFleet", params, headers=headers)
            response = json.loads(body)
            model = models.CopyFleetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAlias(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CreateAlias）用于创建别名。

        :param request: Request instance for CreateAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAsset(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CreateAsset）用于创建生成包。
        通过获取上传cos的临时密钥，将文件上传至cos，然后将生成包的zip名称下发给本接口完成资源创建。

        上传文件至 cos支持俩种方式：

        - 获取预签名方式，COS 简单上传
            1. [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727) 获取预签名信息
            2. 使用 COS API 进行上传([参考文档](https://cloud.tencent.com/document/product/436/7749))
        -  临时密钥方式，COS 简单上传或者分块上传方式
            1. [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727)（获取上传 bucket  第一次调用需要，后续可以不用调用）
            2. [GetUploadFederationToken](https://cloud.tencent.com/document/product/1165/48742) 获取临时密钥
            3. 使用 COS API 进行上传([参考文档](https://cloud.tencent.com/document/product/436/7742))

        具体使用场景可以参考 [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727) ,  [GetUploadFederationToken](https://cloud.tencent.com/document/product/1165/48742)和下面 CreateAsset 示例。

        :param request: Request instance for CreateAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAsset", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssetWithImage(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CreateAssetWithImage）用于创建生成包镜像信息。

        :param request: Request instance for CreateAssetWithImage.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateAssetWithImageRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateAssetWithImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssetWithImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssetWithImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFleet(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CreateFleet）用于创建服务器舰队。

        :param request: Request instance for CreateFleet.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateFleetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateFleetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFleet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFleetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGameServerSession(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CreateGameServerSession）用于创建游戏服务会话。

        :param request: Request instance for CreateGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGameServerSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGameServerSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateGameServerSessionQueue(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（CreateGameServerSessionQueue）用于创建游戏服务器会话队列。

        :param request: Request instance for CreateGameServerSessionQueue.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionQueueRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateGameServerSessionQueue", params, headers=headers)
            response = json.loads(body)
            model = models.CreateGameServerSessionQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAlias(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DeleteAlias）用于删除别名。

        :param request: Request instance for DeleteAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAlias", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAsset(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DeleteAsset）用于删除生成包。

        :param request: Request instance for DeleteAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFleet(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DeleteFleet）用于删除服务器舰队。

        :param request: Request instance for DeleteFleet.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteFleetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteFleetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFleet", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFleetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGameServerSessionQueue(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DeleteGameServerSessionQueue）用于删除游戏服务器会话队列。

        :param request: Request instance for DeleteGameServerSessionQueue.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteGameServerSessionQueueRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteGameServerSessionQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGameServerSessionQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGameServerSessionQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScalingPolicy(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DeleteScalingPolicy）用于删除服务器舰队的扩缩容策略。
        通过服务器舰队ID和策略名称删除服务器舰队的扩缩容策略，只传递服务器舰队ID时，会将这个服务器舰队下的所有策略都删除。
        传递策略名称时，单独删除策略名称对应的策略。

        :param request: Request instance for DeleteScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTimerScalingPolicy(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DeleteTimerScalingPolicy）用于删除fleet下的定时器。

        :param request: Request instance for DeleteTimerScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteTimerScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteTimerScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTimerScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTimerScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAlias(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeAlias）用于获取别名详情。

        :param request: Request instance for DescribeAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlias", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsset(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeAsset）获取生成包信息。

        :param request: Request instance for DescribeAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssetSystems(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeAssetSystems）用于获取生成包支持的操作系统。

        :param request: Request instance for DescribeAssetSystems.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAssetSystemsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAssetSystemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssetSystems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetSystemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssets(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeAssets）用于获取生成包列表。

        :param request: Request instance for DescribeAssets.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAssetsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAssetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnInstances(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeCcnInstances）用于查询云联网实例。

        :param request: Request instance for DescribeCcnInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeCcnInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetAttributes(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetAttributes）用于查询服务器舰队属性。

        :param request: Request instance for DescribeFleetAttributes.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetAttributesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetCapacity(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetCapacity）用于查询服务部署容量配置。

        :param request: Request instance for DescribeFleetCapacity.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetCapacityRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetCapacity", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetCapacityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetEvents(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetEvents）用于查询服务器舰队相关的事件列表。

        :param request: Request instance for DescribeFleetEvents.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetEventsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetPortSettings(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetPortSettings）用于获取服务器舰队安全组信息。

        :param request: Request instance for DescribeFleetPortSettings.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetPortSettingsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetPortSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetPortSettings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetPortSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetRelatedResources(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetRelatedResources）用于获取与游戏服务器舰队关联的资源信息，如别名、队列

        :param request: Request instance for DescribeFleetRelatedResources.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetRelatedResourcesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetRelatedResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetRelatedResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetRelatedResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetStatisticDetails(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetStatisticDetails）用于查询服务部署统计详情。

        :param request: Request instance for DescribeFleetStatisticDetails.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticDetailsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetStatisticDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetStatisticDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetStatisticFlows(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetStatisticFlows）用于查询服务部署统计用量。

        :param request: Request instance for DescribeFleetStatisticFlows.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticFlowsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetStatisticFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetStatisticFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetStatisticSummary(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetStatisticSummary）用于查询服务部署统计汇总信息。

        :param request: Request instance for DescribeFleetStatisticSummary.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticSummaryRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetStatisticSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetStatisticSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFleetUtilization(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeFleetUtilization）用于查询服务器舰队的利用率信息。

        :param request: Request instance for DescribeFleetUtilization.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetUtilizationRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetUtilizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFleetUtilization", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFleetUtilizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessionDetails(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeGameServerSessionDetails）用于查询游戏服务器会话详情列表。

        :param request: Request instance for DescribeGameServerSessionDetails.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionDetailsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessionDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessionPlacement(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeGameServerSessionPlacement）用于查询游戏服务器会话的放置。

        :param request: Request instance for DescribeGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessionPlacement", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionPlacementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessionQueues(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeGameServerSessionQueues）用于查询游戏服务器会话队列。

        :param request: Request instance for DescribeGameServerSessionQueues.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionQueuesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessionQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGameServerSessions(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeGameServerSessions）用于查询游戏服务器会话列表。

        :param request: Request instance for DescribeGameServerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGameServerSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGameServerSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceLimit(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeInstanceLimit）用于查询用户实例数限额。

        :param request: Request instance for DescribeInstanceLimit.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceLimitRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTypes(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeInstanceTypes）用于获取服务器实例类型列表。

        :param request: Request instance for DescribeInstanceTypes.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceTypesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeInstances）用于查询服务器实例列表。

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesResponse`

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstancesExtend(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeInstancesExtend）用于查询实例扩展信息列表。

        :param request: Request instance for DescribeInstancesExtend.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesExtendRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesExtendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesExtend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesExtendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePlayerSessions(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribePlayerSessions）用于获取玩家会话列表。

        :param request: Request instance for DescribePlayerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribePlayerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribePlayerSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayerSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePlayerSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRuntimeConfiguration(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeRuntimeConfiguration）用于获取服务器舰队运行配置。

        :param request: Request instance for DescribeRuntimeConfiguration.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeRuntimeConfigurationRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeRuntimeConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuntimeConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuntimeConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScalingPolicies(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeScalingPolicies）用于查询服务器舰队的动态扩缩容策略列表。

        :param request: Request instance for DescribeScalingPolicies.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScalingPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScalingPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTimerScalingPolicies(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeTimerScalingPolicies）用于查询fleet下的定时器列表。可以通过fleetid，定时器名称分页查询。

        :param request: Request instance for DescribeTimerScalingPolicies.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeTimerScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeTimerScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTimerScalingPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTimerScalingPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserQuota(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeUserQuota）获取用户单个模块配额。

        :param request: Request instance for DescribeUserQuota.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotaRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserQuotas(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DescribeUserQuotas）用于获取用户配额

        :param request: Request instance for DescribeUserQuotas.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserQuotas", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserQuotasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachCcnInstances(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（DetachCcnInstances）用于解关联云联网实例。

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EndGameServerSessionAndProcess(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（EndGameServerSessionAndProcess）用于终止游戏服务器会话和对应的进程，适用于时限保护和不保护。

        :param request: Request instance for EndGameServerSessionAndProcess.
        :type request: :class:`tencentcloud.gse.v20191112.models.EndGameServerSessionAndProcessRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.EndGameServerSessionAndProcessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EndGameServerSessionAndProcess", params, headers=headers)
            response = json.loads(body)
            model = models.EndGameServerSessionAndProcessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGameServerInstanceLogUrl(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口用于获取游戏服务器实例的日志URL。

        :param request: Request instance for GetGameServerInstanceLogUrl.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetGameServerInstanceLogUrlRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetGameServerInstanceLogUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGameServerInstanceLogUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetGameServerInstanceLogUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetGameServerSessionLogUrl(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（GetGameServerSessionLogUrl）用于获取游戏服务器会话的日志URL。

        :param request: Request instance for GetGameServerSessionLogUrl.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetGameServerSessionLogUrlRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetGameServerSessionLogUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetGameServerSessionLogUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetGameServerSessionLogUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInstanceAccess(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（GetInstanceAccess）用于获取实例登录所需要的凭据。

        :param request: Request instance for GetInstanceAccess.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetInstanceAccessRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetInstanceAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInstanceAccess", params, headers=headers)
            response = json.loads(body)
            model = models.GetInstanceAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUploadCredentials(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（GetUploadCredentials）获取上传文件授权信息。
        通过 [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727) 接口获取临时授权信息后，调用 COS API将数据上传，根据上传的 BucketKey 信息进行生成包 [CreateAsset](https://cloud.tencent.com/document/product/1165/48731) 的创建。参考下面的示例部分。

        :param request: Request instance for GetUploadCredentials.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetUploadCredentialsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetUploadCredentialsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUploadCredentials", params, headers=headers)
            response = json.loads(body)
            model = models.GetUploadCredentialsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUploadFederationToken(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（GetUploadFederationToken）用于 获取生成包上传所需要的临时密钥。

        :param request: Request instance for GetUploadFederationToken.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetUploadFederationTokenRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetUploadFederationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUploadFederationToken", params, headers=headers)
            response = json.loads(body)
            model = models.GetUploadFederationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def JoinGameServerSession(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（JoinGameServerSession）用于加入游戏服务器会话。

        :param request: Request instance for JoinGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("JoinGameServerSession", params, headers=headers)
            response = json.loads(body)
            model = models.JoinGameServerSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def JoinGameServerSessionBatch(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（JoinGameServerSessionBatch）用于批量加入游戏服务器会话。

        :param request: Request instance for JoinGameServerSessionBatch.
        :type request: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionBatchRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("JoinGameServerSessionBatch", params, headers=headers)
            response = json.loads(body)
            model = models.JoinGameServerSessionBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAliases(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（ListAliases）用于检索帐户下的所有别名。

        :param request: Request instance for ListAliases.
        :type request: :class:`tencentcloud.gse.v20191112.models.ListAliasesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.ListAliasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAliases", params, headers=headers)
            response = json.loads(body)
            model = models.ListAliasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListFleets(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（ListFleets）用于获取服务器舰队列表。

        :param request: Request instance for ListFleets.
        :type request: :class:`tencentcloud.gse.v20191112.models.ListFleetsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.ListFleetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListFleets", params, headers=headers)
            response = json.loads(body)
            model = models.ListFleetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutScalingPolicy(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（PutScalingPolicy）用于设置服务器舰队的动态扩缩容策略。

        通过此接口可以增加或者更新服务器舰队的扩缩容策略。
        服务器舰队可以有多个扩缩容策略，但是只有一个TargetBased基于目标的策略。

        ## TargetBased基于目标的策略

        TargetBased策略计算的指标是PercentAvailableGameSessions，这个策略用于计算当前服务器舰队应该有多少个CVM实例来支撑和分配游戏会话。
        PercentAvailableGameSessions表示服务器舰队的缓冲值；用来计算服务器舰队在当前容量下可以处理的额外玩家会话数量。
        如果使用基于目标的策略，可以按照业务需求设置一个期望的缓冲区大小，GSE的会按照配置的策略来扩容和缩容到这个目标要求的CVM实例数。

        例如：客户可以设置同时承载100个游戏会话的服务器舰队预留10%的缓冲区。GSE会按照这个策略执行时，若服务器舰队的可用容量低于或高于10%的游戏服务器会话时，执行扩缩容动作。
        GSE按照策略期望，扩容新CVM实例或缩容未使用的实例，保持在10%左右的缓冲区。

        #### 请求参数取值说明

        ```
        Name取值策略名称，
        FleetId取值为选择的服务器舰队ID，
        PolicyType取值TargetBased，
        MetricName取值PercentAvailableGameSessions，
        TargetConfiguration取值为所需的缓冲区值对象，
        其他参数不用传递。
        请求成功时，将返回策略名称。扩缩容策略在成功创建立即自动生效。
        ```



        ## RuleBased基于规则的策略

        ####  请求参数取值说明

        ```
        Name取值策略名称，
        FleetId取值为选择的服务器舰队ID，
        PolicyType取值RuleBased，
        MetricName取值（AvailableGameServerSessions，AvailableCustomCount，PercentAvailableCustomCount，ActiveInstances，IdleInstances，CurrentPlayerSessions和PercentIdleInstances）说明见备注1，
        其他参数不用传递。
        ComparisonOperator取值为 >,>=,<,<=这4个比较符号中的一个，
        Threshold取值为指标MetricName达到的阈值是多少，
        EvaluationPeriods取值为指标MetricName达到的阈值持续了多少时间，单位是分钟，
        ScalingAdjustmentType取值（ChangeInCapacity，ExactCapacity，PercentChangeInCapacity）说明见备注2
        ScalingAdjustment取值为指标MetricName达到的阈值的条件后，扩缩容多少个CVM实例。
        请求成功时，将返回策略名称。扩缩容策略在成功创建立即自动生效。
        ```

        规则执行的条件表达式如下所示：

        ```
        若 [MetricName] 是 [ComparisonOperator] [Threshold] 持续 [EvaluationPeriods] 分钟, 则 [ScalingAdjustmentType] 调整 [ScalingAdjustment]个实例。
        ```
        ```
        if [MetricName] ComparisonOperator [Threshold] for [EvaluationPeriods] minutes, then scaling up by/to  [ScalingAdjustment]
        ```
        例如1：如果当前AvailableCustomCount值大于等于10，持续5分钟，扩容1台CVM实例。
        ```
        ScalingAdjustmentType = ChangeInCapacity
        if [AvailableGameServerSessions] >= [10] for [5] minutes, then scaling up [1]
        ```
        例如2：如果当前AvailableGameServerSessions值大于等于200，持续5分钟，扩容到2台CVM实例。
        ```
        ScalingAdjustmentType = ExactCapacity
        if [AvailableGameServerSessions] >= [200] for [5] minutes, then scaling to [2]
        ```
        例如3：如果当前AvailableCustomCount值大于等于400，持续5分钟，扩容20%台CVM实例。
        当前CVM实例数为10台。扩容20%台CVM实例就是增加 10*20%等于2台
        ```
        ScalingAdjustmentType = PercentChangeInCapacity
        if [AvailableGameServerSessions] >= [400] for [5] minutes, then scaling by [currentCVMCount * 20 %]
        ```
        **备注1**

        - | 策略名称（MetricName）                                       | 计算公式                                   | 场景                                        | 场景使用举例                                                 |
          | :----------------------------------------------------------- | :----------------------------------------- | :------------------------------------------ | :----------------------------------------------------------- |
          | CurrentPlayerSessions<br>当前玩家数指标                      | = 当前在线的玩家数                         | CVM随着玩家会话数变化做扩缩容。             | 例如：<br>MetricName: CurrentPlayerSessions<br>ComparisonOperator: '<=' <br>Threshold: 300<br/>EvaluationPeriods: 1<br/>ScalingAdjustment: 2<br/>ScalingAdjustment: ChangeInCapacity<br>说明：若当前CurrentPlayerSessions小于等于300，持续1分钟，则扩容2台CVM。 |
          | AvailableGameServerSessions<br>可用游戏服务器会话数          | = 可用游戏服务会话数                       | CVM随着可用游戏会话数变化做扩缩容。         | 例如：<br/>MetricName: AvailableGameServerSessions<br/>ComparisonOperator: '<' <br/>Threshold: 50<br/>EvaluationPeriods: 5<br/>ScalingAdjustment: 2<br/>ScalingAdjustment: ExactCapacity<br/>说明：若当前AvailableGameServerSessions小于50，持续5分钟，则扩容到2台CVM。 |
          | PercentAvailableGameServerSessions<br>可用游戏服务器会话百分比 | = 空闲游戏会话数 / 所有的游戏会话数 * 100% | CVM随着可用游戏会话数百分比变化做扩缩容。   | 例如：<br/>MetricName: PercentAvailableGameServerSessions<br/>ComparisonOperator: '<' <br/>Threshold: 50<br/>EvaluationPeriods: 1<br/>ScalingAdjustment: -30<br/>ScalingAdjustment: PercentChangeInCapacity<br/>说明：若当前PercentAvailableGameServerSessions小于50%，持续1分钟，则缩容当前实例数30%台CVM。 |
          | AvailableCustomCount<br>可用客户自定义数指标                 | = 客户自定义的数                           | CVM随着可用客户自定义数变化做扩缩容。       | 例如：<br/>MetricName: AvailableCustomCount<br/>ComparisonOperator: '>=' <br/>Threshold: 6<br/>EvaluationPeriods: 3<br/>ScalingAdjustment: -1<br/>ScalingAdjustment: ExactCapacity<br/>说明：若当前AvailableCustomCount大于等于6，持续3分钟，则缩容到1台CVM。 |
          | PercentAvailableCustomCount<br>可用客户自定义数百分比        | = 客户自定义数 / 客户最大自定义数* 100%    | CVM随着可用客户自定义数百分比变化做扩缩容。 | 例如：<br/>MetricName: PercentAvailableCustomCount<br/>ComparisonOperator: '<' <br/>Threshold: 15<br/>EvaluationPeriods: 3<br/>ScalingAdjustment: 1<br/>ScalingAdjustment: ChangeInCapacity<br/>说明：若当前PercentAvailableCustomCount小于15%，持续3分钟，则扩容1台CVM。 |
          | ActiveInstances<br>活跃实例数指标                            | = 总实例数 - 缩容中的实例数                | CVM随着活跃实例数变化做扩缩容。             | 例如：<br/>MetricName: ActiveInstances<br/>ComparisonOperator: '<' <br/>Threshold: 3<br/>EvaluationPeriods: 1<br/>ScalingAdjustment: 3<br/>ScalingAdjustment: ExactCapacity<br/>说明：若当前ActiveInstances小于3台，持续1分钟，则扩容保留到3台CVM。 |
          | IdleInstances<br>空闲实例数指标                              | = 未使用的进程数 / 每实例进程数            | CVM随着空闲实例数变化做扩缩容。             | 例如：<br/>MetricName: IdleInstances<br/>ComparisonOperator: '<' <br/>Threshold: 2<br/>EvaluationPeriods: 3<br/>ScalingAdjustment: 1<br/>ScalingAdjustment: ChangeInCapacity<br/>说明：若当前IdleInstances小于2台，持续3分钟，则扩容1台CVM。 |
          | PercentIdleInstances<br>空闲实例百分比                       | = IdleInstances / ActiveInstances * 100%   | CVM随着空闲实例百分比变化做扩缩容。         | 例如：<br/>MetricName: PercentIdleInstances<br/>ComparisonOperator: '<' <br/>Threshold: 50<br/>EvaluationPeriods: 3<br/>ScalingAdjustment: 1<br/>ScalingAdjustment: ChangeInCapacity<br/>说明：若当前PercentIdleInstances小于50%，持续3分钟，则扩容1台CVM。 |



        **备注2**

        **ChangeInCapacity**

            当前CVM实例个数的扩容或缩容的调整值。正值按值扩容，负值按值缩容。

        **ExactCapacity**

            把当前CVM实例个数调整为ScalingAdjustment设置的CVM实例数。

        **PercentChangeInCapacity**

            按比例增加或减少的百分比。正值按比例扩容，负值按比例缩容；例如，值“-10”将按10%的比例缩容CVM实例。

        :param request: Request instance for PutScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.PutScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.PutScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.PutScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def PutTimerScalingPolicy(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（PutTimerScalingPolicy）用于给fleet创建或更新定时器。

        填写字段timer_id，表示更新；不填字段timer_id表示新增。

        :param request: Request instance for PutTimerScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.PutTimerScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.PutTimerScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PutTimerScalingPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.PutTimerScalingPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResolveAlias(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（ResolveAlias）用于获取别名当前指向的fleetId。

        :param request: Request instance for ResolveAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.ResolveAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.ResolveAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResolveAlias", params, headers=headers)
            response = json.loads(body)
            model = models.ResolveAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchGameServerSessions(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（SearchGameServerSessions）用于搜索游戏服务器会话列表。

        :param request: Request instance for SearchGameServerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.SearchGameServerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SearchGameServerSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchGameServerSessions", params, headers=headers)
            response = json.loads(body)
            model = models.SearchGameServerSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetServerReserved(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（SetServerReserved）用于将异常的实例标记为保留，用于问题排查。

        字段ReserveValue：0默认值，不保留；1 保留

        :param request: Request instance for SetServerReserved.
        :type request: :class:`tencentcloud.gse.v20191112.models.SetServerReservedRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SetServerReservedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetServerReserved", params, headers=headers)
            response = json.loads(body)
            model = models.SetServerReservedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetServerWeight(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（SetServerWeight）用于设置服务器权重。

        :param request: Request instance for SetServerWeight.
        :type request: :class:`tencentcloud.gse.v20191112.models.SetServerWeightRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SetServerWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetServerWeight", params, headers=headers)
            response = json.loads(body)
            model = models.SetServerWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartFleetActions(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（StartFleetActions）用于启用服务器舰队自动扩缩容。

        :param request: Request instance for StartFleetActions.
        :type request: :class:`tencentcloud.gse.v20191112.models.StartFleetActionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StartFleetActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartFleetActions", params, headers=headers)
            response = json.loads(body)
            model = models.StartFleetActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartGameServerSessionPlacement(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（StartGameServerSessionPlacement）用于开始放置游戏服务器会话。

        :param request: Request instance for StartGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.StartGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StartGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartGameServerSessionPlacement", params, headers=headers)
            response = json.loads(body)
            model = models.StartGameServerSessionPlacementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopFleetActions(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（StopFleetActions）用于停止服务器舰队自动扩缩容，改为手动扩缩容。

        :param request: Request instance for StopFleetActions.
        :type request: :class:`tencentcloud.gse.v20191112.models.StopFleetActionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StopFleetActionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopFleetActions", params, headers=headers)
            response = json.loads(body)
            model = models.StopFleetActionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopGameServerSessionPlacement(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（StopGameServerSessionPlacement）用于停止放置游戏服务器会话。

        :param request: Request instance for StopGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.StopGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StopGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopGameServerSessionPlacement", params, headers=headers)
            response = json.loads(body)
            model = models.StopGameServerSessionPlacementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAlias(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateAlias）用于更新别名的属性。

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAlias", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAliasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAsset(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateAsset）用于修改生成包信息。

        :param request: Request instance for UpdateAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateAssetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAsset", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAssetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBucketAccelerateOpt(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateBucketAccelerateOpt）用于开启cos全球加速。

        :param request: Request instance for UpdateBucketAccelerateOpt.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateBucketAccelerateOptRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateBucketAccelerateOptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBucketAccelerateOpt", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBucketAccelerateOptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateBucketCORSOpt(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateBucketCORSOpt）用于设置cos跨域访问。

        :param request: Request instance for UpdateBucketCORSOpt.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateBucketCORSOptRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateBucketCORSOptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateBucketCORSOpt", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateBucketCORSOptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFleetAttributes(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateFleetAttributes）用于更新服务器舰队属性。

        :param request: Request instance for UpdateFleetAttributes.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetAttributesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFleetAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFleetAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFleetCapacity(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateFleetCapacity）用于更新服务器舰队容量配置。

        :param request: Request instance for UpdateFleetCapacity.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetCapacityRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetCapacityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFleetCapacity", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFleetCapacityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFleetName(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateFleetName）用于更新服务器舰队名称。

        :param request: Request instance for UpdateFleetName.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetNameRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFleetName", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFleetNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateFleetPortSettings(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateFleetPortSettings）用于更新服务器舰队安全组。

        :param request: Request instance for UpdateFleetPortSettings.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetPortSettingsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetPortSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateFleetPortSettings", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateFleetPortSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGameServerSession(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateGameServerSession）用于更新游戏服务器会话。

        :param request: Request instance for UpdateGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGameServerSession", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGameServerSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateGameServerSessionQueue(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateGameServerSessionQueue）用于修改游戏服务器会话队列。

        :param request: Request instance for UpdateGameServerSessionQueue.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionQueueRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateGameServerSessionQueue", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateGameServerSessionQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRuntimeConfiguration(self, request):
        """此接口无法使用，游戏服务器引擎GSE已于6.1正式下架，感谢您的支持

        本接口（UpdateRuntimeConfiguration）用于更新服务器舰队配置。

        :param request: Request instance for UpdateRuntimeConfiguration.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateRuntimeConfigurationRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateRuntimeConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRuntimeConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRuntimeConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))