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
from tencentcloud.gse.v20191112 import models


class GseClient(AbstractClient):
    _apiVersion = '2019-11-12'
    _endpoint = 'gse.tencentcloudapi.com'


    def AttachCcnInstances(self, request):
        """本接口（AttachCcnInstances）用于关联云联网实例

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachCcnInstancesResponse()
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


    def CreateAlias(self, request):
        """本接口（CreateAlias）用于创建别名

        :param request: Request instance for CreateAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAliasResponse()
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


    def CreateAsset(self, request):
        """本接口（CreateAsset）用于创建生成包。
        通过获取上传cos的临时密钥，将文件上传至cos，然后将生成包的zip名称下发给[CreateAsset](https://cloud.tencent.com/document/product/1165/48731)完成接口创建。上传文件至 cos支持俩种方式：

        - 获取预签名方式，COS 简单上传
            1. [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727) 获取预签名信息
            2. 使用 COS API 进行上传
        -  临时密钥方式，COS 简单上传或者分块上传方式
            1. [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727)（获取上传 bucket  第一次调用需要，后续可以不用调用）
            2. [GetUploadFederationToken](https://cloud.tencent.com/document/product/1165/48742) 获取临时密钥
            3. 使用 COS API 进行上传

        具体使用场景可以参考 [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727) ,  [GetUploadFederationToken](https://cloud.tencent.com/document/product/1165/48742)和下面 CreateAsset 示例。

        :param request: Request instance for CreateAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssetResponse()
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


    def CreateFleet(self, request):
        """本接口（CreateFleet）用于创建服务器舰队

        :param request: Request instance for CreateFleet.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateFleetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateFleetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFleet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFleetResponse()
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


    def CreateGameServerSession(self, request):
        """本接口（CreateGameServerSession）用于创建游戏服务会话

        :param request: Request instance for CreateGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGameServerSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGameServerSessionResponse()
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


    def CreateGameServerSessionQueue(self, request):
        """本接口（CreateGameServerSessionQueue）用于创建游戏服务器会话队列

        :param request: Request instance for CreateGameServerSessionQueue.
        :type request: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionQueueRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.CreateGameServerSessionQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateGameServerSessionQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateGameServerSessionQueueResponse()
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


    def DeleteAlias(self, request):
        """本接口（DeleteAlias）用于删除别名

        :param request: Request instance for DeleteAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAliasResponse()
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


    def DeleteAsset(self, request):
        """本接口（DeleteAsset）用于删除生成包

        :param request: Request instance for DeleteAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAssetResponse()
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


    def DeleteFleet(self, request):
        """本接口（DeleteFleet）用于删除服务器舰队

        :param request: Request instance for DeleteFleet.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteFleetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteFleetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFleet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFleetResponse()
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


    def DeleteGameServerSessionQueue(self, request):
        """本接口（DeleteGameServerSessionQueue）用于删除游戏服务器会话队列

        :param request: Request instance for DeleteGameServerSessionQueue.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteGameServerSessionQueueRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteGameServerSessionQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteGameServerSessionQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteGameServerSessionQueueResponse()
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


    def DeleteScalingPolicy(self, request):
        """本接口（DeleteScalingPolicy）用于删除扩缩容配置

        :param request: Request instance for DeleteScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.DeleteScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DeleteScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteScalingPolicyResponse()
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


    def DescribeAlias(self, request):
        """本接口（DescribeAlias）用于获取别名详情

        :param request: Request instance for DescribeAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAliasResponse()
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


    def DescribeAsset(self, request):
        """本接口（DescribeAsset）获取生成包信息

        :param request: Request instance for DescribeAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetResponse()
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


    def DescribeAssets(self, request):
        """本接口（DescribeAssets）用于获取生成包列表

        :param request: Request instance for DescribeAssets.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeAssetsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeAssetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssetsResponse()
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


    def DescribeCcnInstances(self, request):
        """本接口（DescribeCcnInstances）用于查询云联网实例

        :param request: Request instance for DescribeCcnInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeCcnInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnInstancesResponse()
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


    def DescribeFleetAttributes(self, request):
        """本接口（DescribeFleetAttributes）用于查询服务器舰队属性

        :param request: Request instance for DescribeFleetAttributes.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetAttributesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetAttributesResponse()
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


    def DescribeFleetCapacity(self, request):
        """用于查询服务部署容量配置

        :param request: Request instance for DescribeFleetCapacity.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetCapacityRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetCapacityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetCapacity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetCapacityResponse()
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


    def DescribeFleetEvents(self, request):
        """本接口（DescribeFleetEvents）用于查询部署服务器舰队相关的事件列表

        :param request: Request instance for DescribeFleetEvents.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetEventsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetEventsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetEvents", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetEventsResponse()
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


    def DescribeFleetPortSettings(self, request):
        """本接口（DescribeFleetPortSettings）用于获取服务器舰队安全组信息

        :param request: Request instance for DescribeFleetPortSettings.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetPortSettingsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetPortSettingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetPortSettings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetPortSettingsResponse()
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


    def DescribeFleetStatisticDetails(self, request):
        """本接口（DescribeFleetStatisticDetails）用于查询服务部署统计详情

        :param request: Request instance for DescribeFleetStatisticDetails.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticDetailsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetStatisticDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetStatisticDetailsResponse()
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


    def DescribeFleetStatisticFlows(self, request):
        """本接口（DescribeFleetStatisticFlows）用于查询服务部署统计用量

        :param request: Request instance for DescribeFleetStatisticFlows.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticFlowsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticFlowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetStatisticFlows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetStatisticFlowsResponse()
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


    def DescribeFleetStatisticSummary(self, request):
        """本接口（DescribeFleetStatisticSummary）用于查询服务部署统计汇总信息

        :param request: Request instance for DescribeFleetStatisticSummary.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticSummaryRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetStatisticSummaryResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetStatisticSummary", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetStatisticSummaryResponse()
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


    def DescribeFleetUtilization(self, request):
        """本接口（DescribeFleetUtilization）用于查询服务器舰队的利用率信息

        :param request: Request instance for DescribeFleetUtilization.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeFleetUtilizationRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeFleetUtilizationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFleetUtilization", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFleetUtilizationResponse()
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


    def DescribeGameServerSessionDetails(self, request):
        """本接口（DescribeGameServerSessionDetails）用于查询游戏服务器会话详情列表

        :param request: Request instance for DescribeGameServerSessionDetails.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionDetailsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGameServerSessionDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGameServerSessionDetailsResponse()
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


    def DescribeGameServerSessionPlacement(self, request):
        """本接口（DescribeGameServerSessionPlacement）用于查询游戏服务器会话的放置

        :param request: Request instance for DescribeGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGameServerSessionPlacement", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGameServerSessionPlacementResponse()
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


    def DescribeGameServerSessionQueues(self, request):
        """本接口（DescribeGameServerSessionQueues）用于查询游戏服务器会话队列

        :param request: Request instance for DescribeGameServerSessionQueues.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionQueuesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionQueuesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGameServerSessionQueues", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGameServerSessionQueuesResponse()
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


    def DescribeGameServerSessions(self, request):
        """本接口（DescribeGameServerSessions）用于查询游戏服务器会话列表

        :param request: Request instance for DescribeGameServerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeGameServerSessionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGameServerSessions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGameServerSessionsResponse()
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


    def DescribeInstanceLimit(self, request):
        """查询用户实例数限额

        :param request: Request instance for DescribeInstanceLimit.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceLimitRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceLimitResponse()
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


    def DescribeInstanceTypes(self, request):
        """本接口（DescribeInstanceTypes）用于获取服务器实例类型列表

        :param request: Request instance for DescribeInstanceTypes.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceTypesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstanceTypesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstanceTypes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstanceTypesResponse()
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
        """本接口（DescribeInstances）用于查询服务器实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesResponse`

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


    def DescribeInstancesExtend(self, request):
        """本接口（DescribeInstances）用于查询实例扩展信息列表

        :param request: Request instance for DescribeInstancesExtend.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesExtendRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeInstancesExtendResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeInstancesExtend", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeInstancesExtendResponse()
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


    def DescribePlayerSessions(self, request):
        """本接口（DescribePlayerSessions）用于获取玩家会话列表

        :param request: Request instance for DescribePlayerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribePlayerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribePlayerSessionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePlayerSessions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePlayerSessionsResponse()
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


    def DescribeRuntimeConfiguration(self, request):
        """本接口（DescribeRuntimeConfiguration）用于获取服务器舰队运行配置

        :param request: Request instance for DescribeRuntimeConfiguration.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeRuntimeConfigurationRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeRuntimeConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRuntimeConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRuntimeConfigurationResponse()
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


    def DescribeScalingPolicies(self, request):
        """本接口（DescribeScalingPolicies）用于查询服务部署的动态扩缩容配置

        :param request: Request instance for DescribeScalingPolicies.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeScalingPoliciesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeScalingPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeScalingPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeScalingPoliciesResponse()
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


    def DescribeUserQuota(self, request):
        """本接口（DescribeUserQuota）获取用户单个模块配额

        :param request: Request instance for DescribeUserQuota.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotaRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserQuotaResponse()
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


    def DescribeUserQuotas(self, request):
        """本接口（DescribeUserQuotas）用于获取用户配额

        :param request: Request instance for DescribeUserQuotas.
        :type request: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DescribeUserQuotasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserQuotas", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserQuotasResponse()
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


    def DetachCcnInstances(self, request):
        """本接口（DetachCcnInstances）用于解关联云联网实例

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.gse.v20191112.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachCcnInstancesResponse()
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


    def GetGameServerSessionLogUrl(self, request):
        """本接口（GetGameServerSessionLogUrl）用于获取游戏服务器会话的日志URL

        :param request: Request instance for GetGameServerSessionLogUrl.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetGameServerSessionLogUrlRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetGameServerSessionLogUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetGameServerSessionLogUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetGameServerSessionLogUrlResponse()
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


    def GetInstanceAccess(self, request):
        """本接口（GetInstanceAccess）用于获取实例登录所需要的凭据

        :param request: Request instance for GetInstanceAccess.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetInstanceAccessRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetInstanceAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetInstanceAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetInstanceAccessResponse()
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


    def GetUploadCredentials(self, request):
        """本接口（GetUploadCredentials）获取上传文件授权信息。
        通过 [GetUploadCredentials](https://cloud.tencent.com/document/product/1165/48727) 接口获取临时授权信息后，调用 COS API将数据上传，根据上传的 BucketKey 信息进行生成包 [CreateAsset](https://cloud.tencent.com/document/product/1165/48731) 的创建。参考下面的示例部分。

        :param request: Request instance for GetUploadCredentials.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetUploadCredentialsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetUploadCredentialsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUploadCredentials", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUploadCredentialsResponse()
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


    def GetUploadFederationToken(self, request):
        """本接口（GetUploadFederationToken）用于 获取生成包上传所需要的临时密钥

        :param request: Request instance for GetUploadFederationToken.
        :type request: :class:`tencentcloud.gse.v20191112.models.GetUploadFederationTokenRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.GetUploadFederationTokenResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetUploadFederationToken", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetUploadFederationTokenResponse()
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


    def JoinGameServerSession(self, request):
        """本接口（JoinGameServerSession）用于加入游戏服务器会话

        :param request: Request instance for JoinGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("JoinGameServerSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.JoinGameServerSessionResponse()
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


    def JoinGameServerSessionBatch(self, request):
        """本接口（JoinGameServerSessionBatch）用于加入游戏服务器会话

        :param request: Request instance for JoinGameServerSessionBatch.
        :type request: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionBatchRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.JoinGameServerSessionBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("JoinGameServerSessionBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.JoinGameServerSessionBatchResponse()
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


    def ListAliases(self, request):
        """本接口（ListAliases）用于检索帐户下的所有别名

        :param request: Request instance for ListAliases.
        :type request: :class:`tencentcloud.gse.v20191112.models.ListAliasesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.ListAliasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListAliases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListAliasesResponse()
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


    def ListFleets(self, request):
        """本接口（ListFleets）用于获取服务器舰队列表

        :param request: Request instance for ListFleets.
        :type request: :class:`tencentcloud.gse.v20191112.models.ListFleetsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.ListFleetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListFleets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListFleetsResponse()
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


    def PutScalingPolicy(self, request):
        """本接口（PutScalingPolicy）用于设置动态扩缩容配置

        :param request: Request instance for PutScalingPolicy.
        :type request: :class:`tencentcloud.gse.v20191112.models.PutScalingPolicyRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.PutScalingPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutScalingPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutScalingPolicyResponse()
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


    def ResolveAlias(self, request):
        """本接口（ResolveAlias）用于获取别名当前指向的fleetId

        :param request: Request instance for ResolveAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.ResolveAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.ResolveAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResolveAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResolveAliasResponse()
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


    def SearchGameServerSessions(self, request):
        """本接口（SearchGameServerSessions）用于搜索游戏服务器会话列表

        :param request: Request instance for SearchGameServerSessions.
        :type request: :class:`tencentcloud.gse.v20191112.models.SearchGameServerSessionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SearchGameServerSessionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchGameServerSessions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchGameServerSessionsResponse()
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


    def SetServerWeight(self, request):
        """设置服务器权重

        :param request: Request instance for SetServerWeight.
        :type request: :class:`tencentcloud.gse.v20191112.models.SetServerWeightRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.SetServerWeightResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetServerWeight", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetServerWeightResponse()
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


    def StartFleetActions(self, request):
        """本接口（StartFleetActions）用于启用服务器舰队自动扩缩容

        :param request: Request instance for StartFleetActions.
        :type request: :class:`tencentcloud.gse.v20191112.models.StartFleetActionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StartFleetActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartFleetActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartFleetActionsResponse()
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


    def StartGameServerSessionPlacement(self, request):
        """本接口（StartGameServerSessionPlacement）用于开始放置游戏服务器会话

        :param request: Request instance for StartGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.StartGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StartGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartGameServerSessionPlacement", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartGameServerSessionPlacementResponse()
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


    def StopFleetActions(self, request):
        """本接口（StopFleetActions）用于停止服务器舰队自动扩缩容，改为手动扩缩容

        :param request: Request instance for StopFleetActions.
        :type request: :class:`tencentcloud.gse.v20191112.models.StopFleetActionsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StopFleetActionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopFleetActions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopFleetActionsResponse()
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


    def StopGameServerSessionPlacement(self, request):
        """本接口（StopGameServerSessionPlacement）用于停止放置游戏服务器会话

        :param request: Request instance for StopGameServerSessionPlacement.
        :type request: :class:`tencentcloud.gse.v20191112.models.StopGameServerSessionPlacementRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.StopGameServerSessionPlacementResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopGameServerSessionPlacement", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopGameServerSessionPlacementResponse()
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


    def UpdateAlias(self, request):
        """本接口（UpdateAlias）用于更新别名的属性

        :param request: Request instance for UpdateAlias.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateAliasRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateAliasResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAlias", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAliasResponse()
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


    def UpdateAsset(self, request):
        """本接口（UpdateAsset）用于修改生成包信息

        :param request: Request instance for UpdateAsset.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateAssetRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateAssetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateAsset", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateAssetResponse()
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


    def UpdateFleetAttributes(self, request):
        """本接口（UpdateFleetAttributes）用于更新服务器舰队属性

        :param request: Request instance for UpdateFleetAttributes.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetAttributesRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFleetAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFleetAttributesResponse()
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


    def UpdateFleetCapacity(self, request):
        """用于更新服务部署容量配置

        :param request: Request instance for UpdateFleetCapacity.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetCapacityRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetCapacityResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFleetCapacity", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFleetCapacityResponse()
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


    def UpdateFleetPortSettings(self, request):
        """本接口（UpdateFleetPortSettings）用于更新服务器舰队安全组

        :param request: Request instance for UpdateFleetPortSettings.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateFleetPortSettingsRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateFleetPortSettingsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateFleetPortSettings", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateFleetPortSettingsResponse()
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


    def UpdateGameServerSession(self, request):
        """本接口（UpdateGameServerSession）用于更新游戏服务器会话

        :param request: Request instance for UpdateGameServerSession.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateGameServerSession", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGameServerSessionResponse()
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


    def UpdateGameServerSessionQueue(self, request):
        """本接口（UpdateGameServerSessionQueue）用于修改游戏服务器会话队列

        :param request: Request instance for UpdateGameServerSessionQueue.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionQueueRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateGameServerSessionQueueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateGameServerSessionQueue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateGameServerSessionQueueResponse()
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


    def UpdateRuntimeConfiguration(self, request):
        """本接口（UpdateRuntimeConfiguration）用于更新服务器舰队配置

        :param request: Request instance for UpdateRuntimeConfiguration.
        :type request: :class:`tencentcloud.gse.v20191112.models.UpdateRuntimeConfigurationRequest`
        :rtype: :class:`tencentcloud.gse.v20191112.models.UpdateRuntimeConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateRuntimeConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateRuntimeConfigurationResponse()
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