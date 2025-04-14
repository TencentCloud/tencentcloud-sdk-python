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
from tencentcloud.ckafka.v20190819 import models


class CkafkaClient(AbstractClient):
    _apiVersion = '2019-08-19'
    _endpoint = 'ckafka.tencentcloudapi.com'
    _service = 'ckafka'


    def AuthorizeToken(self, request):
        """给实例授权token

        :param request: Request instance for AuthorizeToken.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.AuthorizeTokenRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.AuthorizeTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuthorizeToken", params, headers=headers)
            response = json.loads(body)
            model = models.AuthorizeTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchCreateAcl(self, request):
        """批量添加ACL策略

        :param request: Request instance for BatchCreateAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.BatchCreateAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchCreateAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateAcl", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyGroupOffsets(self, request):
        """批量修改消费组offset

        :param request: Request instance for BatchModifyGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BatchModifyTopicAttributes(self, request):
        """批量设置主题属性

        :param request: Request instance for BatchModifyTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.BatchModifyTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyTopicAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyTopicAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelAuthorizationToken(self, request):
        """取消授权token

        :param request: Request instance for CancelAuthorizationToken.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CancelAuthorizationTokenRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CancelAuthorizationTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelAuthorizationToken", params, headers=headers)
            response = json.loads(body)
            model = models.CancelAuthorizationTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckCdcCluster(self, request):
        """用于查询cdc-ckafka任务状态

        :param request: Request instance for CheckCdcCluster.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CheckCdcClusterRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CheckCdcClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckCdcCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CheckCdcClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAcl(self, request):
        """添加 ACL 策略

        :param request: Request instance for CreateAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAclRule(self, request):
        """添加 ACL 规则

        :param request: Request instance for CreateAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdcCluster(self, request):
        """用于cdc的专用ckafka集群

        :param request: Request instance for CreateCdcCluster.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateCdcClusterRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateCdcClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdcCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdcClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConnectResource(self, request):
        """创建Datahub连接源

        :param request: Request instance for CreateConnectResource.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateConnectResourceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateConnectResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConnectResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConnectResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateConsumer(self, request):
        """创建消费者组

        :param request: Request instance for CreateConsumer.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateConsumerRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateConsumerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsumer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsumerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatahubTask(self, request):
        """创建DIP转储任务

        :param request: Request instance for CreateDatahubTask.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTaskRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatahubTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatahubTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatahubTopic(self, request):
        """创建DIP主题

        :param request: Request instance for CreateDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstancePost(self, request):
        """由于出参需要更新，当前接口将会在未来版本中废弃，建议用户迁移使用 CreatePostPaidInstance 接口。创建按量计费实例。通常用于 SDK 或云 API 控制台调用接口，创建后付费 CKafka 实例。调用接口与在 CKafka 控制台购买按量付费实例效果相同。

        :param request: Request instance for CreateInstancePost.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstancePost", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancePostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInstancePre(self, request):
        """创建实例(预付费包年包月),  仅支持创建专业版实例

        :param request: Request instance for CreateInstancePre.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateInstancePreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstancePre", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancePreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePartition(self, request):
        """本接口用于增加主题中的分区

        :param request: Request instance for CreatePartition.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreatePartitionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreatePartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePartition", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePostPaidInstance(self, request):
        """当前接口用来替代 CreateInstancePost 接口。创建按量计费实例。通常用于 SDK 或云 API 控制台调用接口，创建后付费 CKafka 实例。调用接口与在 CKafka 控制台购买按量付费实例效果相同。

        :param request: Request instance for CreatePostPaidInstance.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreatePostPaidInstanceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreatePostPaidInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePostPaidInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePostPaidInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrometheus(self, request):
        """添加普罗米修斯监控1

        :param request: Request instance for CreatePrometheus.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreatePrometheusRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreatePrometheusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrometheus", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrometheusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoute(self, request):
        """添加实例路由

        :param request: Request instance for CreateRoute.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateRouteRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoute", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateToken(self, request):
        """创建最高权限的token

        :param request: Request instance for CreateToken.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTokenRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopic(self, request):
        """创建ckafka主题

        :param request: Request instance for CreateTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopic", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTopicIpWhiteList(self, request):
        """创建主题ip白名单

        :param request: Request instance for CreateTopicIpWhiteList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicIpWhiteListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateTopicIpWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTopicIpWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTopicIpWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        """添加用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAcl(self, request):
        """删除ACL

        :param request: Request instance for DeleteAcl.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAcl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAclRule(self, request):
        """删除ACL规则

        :param request: Request instance for DeleteAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteConnectResource(self, request):
        """删除Datahub连接源

        :param request: Request instance for DeleteConnectResource.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteConnectResourceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteConnectResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteConnectResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteConnectResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDatahubTask(self, request):
        """删除Dip任务

        :param request: Request instance for DeleteDatahubTask.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteDatahubTaskRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteDatahubTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDatahubTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatahubTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDatahubTopic(self, request):
        """删除DIP主题

        :param request: Request instance for DeleteDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteGroup(self, request):
        """删除消费组

        :param request: Request instance for DeleteGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstancePost(self, request):
        """删除后付费实例

        :param request: Request instance for DeleteInstancePost.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteInstancePostRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteInstancePostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstancePost", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstancePostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInstancePre(self, request):
        """删除预付费实例，该接口会对实例执行隔离并删除的动作，执行成功后实例会被直接删除销毁

        :param request: Request instance for DeleteInstancePre.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteInstancePreRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteInstancePreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInstancePre", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInstancePreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoute(self, request):
        """删除路由

        :param request: Request instance for DeleteRoute.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRouteTriggerTime(self, request):
        """修改删除路由延迟触发时间

        :param request: Request instance for DeleteRouteTriggerTime.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteTriggerTimeRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteRouteTriggerTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRouteTriggerTime", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteTriggerTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopic(self, request):
        """删除ckafka主题

        :param request: Request instance for DeleteTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTopicIpWhiteList(self, request):
        """删除主题IP白名单

        :param request: Request instance for DeleteTopicIpWhiteList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicIpWhiteListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteTopicIpWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTopicIpWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTopicIpWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        """删除用户

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeACL(self, request):
        """枚举ACL

        :param request: Request instance for DescribeACL.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeACLRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeACLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeACL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeACLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAclRule(self, request):
        """查询ACL规则列表

        :param request: Request instance for DescribeAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAppInfo(self, request):
        """查询用户列表

        :param request: Request instance for DescribeAppInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeAppInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeAppInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAppInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAppInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCkafkaZone(self, request):
        """用于查看ckafka的可用区列表

        :param request: Request instance for DescribeCkafkaZone.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeCkafkaZoneRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeCkafkaZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCkafkaZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCkafkaZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConnectResource(self, request):
        """查询Datahub连接源

        :param request: Request instance for DescribeConnectResource.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConnectResource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConnectResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConnectResources(self, request):
        """查询Datahub连接源列表

        :param request: Request instance for DescribeConnectResources.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourcesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConnectResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConnectResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConnectResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeConsumerGroup(self, request):
        """查询消费分组信息

        :param request: Request instance for DescribeConsumerGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeConsumerGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeConsumerGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeConsumerGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeConsumerGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCvmInfo(self, request):
        """本接口用于获取实例对应后端CVM信息，包括cvmId和ip等。用于专业版，标准版返回数据为空

        :param request: Request instance for DescribeCvmInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeCvmInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeCvmInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCvmInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCvmInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubGroupOffsets(self, request):
        """获取Datahub消费分组offset

        :param request: Request instance for DescribeDatahubGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubTask(self, request):
        """查询Datahub任务信息

        :param request: Request instance for DescribeDatahubTask.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTaskRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubTasks(self, request):
        """查询Datahub任务列表

        :param request: Request instance for DescribeDatahubTasks.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTasksRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubTopic(self, request):
        """获取DIP主题属性

        :param request: Request instance for DescribeDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatahubTopics(self, request):
        """查询DIP主题列表

        :param request: Request instance for DescribeDatahubTopics.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeDatahubTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatahubTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatahubTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroup(self, request):
        """枚举消费分组(精简版)

        :param request: Request instance for DescribeGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupInfo(self, request):
        """获取消费分组信息

        :param request: Request instance for DescribeGroupInfo.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupInfoRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGroupOffsets(self, request):
        """获取消费分组offset

        :param request: Request instance for DescribeGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceAttributes(self, request):
        """获取实例属性

        :param request: Request instance for DescribeInstanceAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """本接口（DescribeInstance）用于在用户账户下获取消息队列 CKafka 实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesResponse`

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


    def DescribeInstancesDetail(self, request):
        """用户账户下获取实例列表详情

        :param request: Request instance for DescribeInstancesDetail.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesDetailRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeInstancesDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstancesDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrometheus(self, request):
        """获取实例Prometheus信息

        :param request: Request instance for DescribePrometheus.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribePrometheusRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribePrometheusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrometheus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrometheusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegion(self, request):
        """枚举地域,只支持广州地域

        :param request: Request instance for DescribeRegion.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeRegionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeRegionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoute(self, request):
        """查看路由信息

        :param request: Request instance for DescribeRoute.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeRouteRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """查询任务状态

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTaskStatusResponse`

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


    def DescribeTopic(self, request):
        """接口请求域名：https://ckafka.tencentcloudapi.com
        本接口（DescribeTopic）用于在用户获取消息队列 CKafka 实例的主题列表

        :param request: Request instance for DescribeTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopic", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicAttributes(self, request):
        """获取主题属性

        :param request: Request instance for DescribeTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicDetail(self, request):
        """获取主题列表详情（仅控制台调用）

        :param request: Request instance for DescribeTopicDetail.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicDetailRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicFlowRanking(self, request):
        """获取Topic流量排行，消费者流量排行

        :param request: Request instance for DescribeTopicFlowRanking.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicFlowRankingRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicFlowRankingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicFlowRanking", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicFlowRankingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicProduceConnection(self, request):
        """查询topic 生产端连接信息

        :param request: Request instance for DescribeTopicProduceConnection.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicProduceConnectionRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicProduceConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicProduceConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicProduceConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicSubscribeGroup(self, request):
        """查询订阅某主题消息分组信息

        :param request: Request instance for DescribeTopicSubscribeGroup.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSubscribeGroupRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSubscribeGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicSubscribeGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicSubscribeGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTopicSyncReplica(self, request):
        """获取Topic 副本详情信息

        :param request: Request instance for DescribeTopicSyncReplica.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSyncReplicaRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTopicSyncReplicaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopicSyncReplica", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopicSyncReplicaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTypeInstances(self, request):
        """本接口（DescribeTypeInstances）用于在用户账户下获取指定类型消息队列 CKafka 实例列表

        :param request: Request instance for DescribeTypeInstances.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeTypeInstancesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeTypeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTypeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTypeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUser(self, request):
        """查询用户信息

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchDatahubMessageByOffset(self, request):
        """根据指定offset位置的消息

        :param request: Request instance for FetchDatahubMessageByOffset.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchDatahubMessageByOffsetRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchDatahubMessageByOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchDatahubMessageByOffset", params, headers=headers)
            response = json.loads(body)
            model = models.FetchDatahubMessageByOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchLatestDatahubMessageList(self, request):
        """查询最新消息列表

        :param request: Request instance for FetchLatestDatahubMessageList.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchLatestDatahubMessageListRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchLatestDatahubMessageListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchLatestDatahubMessageList", params, headers=headers)
            response = json.loads(body)
            model = models.FetchLatestDatahubMessageListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchMessageByOffset(self, request):
        """根据指定offset位置的消息

        :param request: Request instance for FetchMessageByOffset.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageByOffsetRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageByOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchMessageByOffset", params, headers=headers)
            response = json.loads(body)
            model = models.FetchMessageByOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchMessageListByOffset(self, request):
        """根据位点查询消息列表

        :param request: Request instance for FetchMessageListByOffset.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageListByOffsetRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageListByOffsetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchMessageListByOffset", params, headers=headers)
            response = json.loads(body)
            model = models.FetchMessageListByOffsetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FetchMessageListByTimestamp(self, request):
        """根据时间戳查询消息列表

        :param request: Request instance for FetchMessageListByTimestamp.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageListByTimestampRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.FetchMessageListByTimestampResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FetchMessageListByTimestamp", params, headers=headers)
            response = json.loads(body)
            model = models.FetchMessageListByTimestampResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquireCkafkaPrice(self, request):
        """Ckafka实例购买/续费询价

        :param request: Request instance for InquireCkafkaPrice.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InquireCkafkaPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquireCkafkaPrice", params, headers=headers)
            response = json.loads(body)
            model = models.InquireCkafkaPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InstanceScalingDown(self, request):
        """按量实例缩容

        :param request: Request instance for InstanceScalingDown.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.InstanceScalingDownRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.InstanceScalingDownResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InstanceScalingDown", params, headers=headers)
            response = json.loads(body)
            model = models.InstanceScalingDownResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAclRule(self, request):
        """修改ACL策略，目前只支持预设规则的是否应用到新增topic这一项的修改

        :param request: Request instance for ModifyAclRule.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyAclRuleRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyConnectResource(self, request):
        """编辑Datahub连接源

        :param request: Request instance for ModifyConnectResource.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyConnectResourceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyConnectResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyConnectResource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyConnectResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatahubTask(self, request):
        """修改Datahub任务

        :param request: Request instance for ModifyDatahubTask.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyDatahubTaskRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyDatahubTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatahubTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatahubTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatahubTopic(self, request):
        """修改DIP主题属性

        :param request: Request instance for ModifyDatahubTopic.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyDatahubTopicRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyDatahubTopicResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatahubTopic", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatahubTopicResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGroupOffsets(self, request):
        """设置Groups 消费分组offset

        :param request: Request instance for ModifyGroupOffsets.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyGroupOffsetsRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyGroupOffsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGroupOffsets", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGroupOffsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceAttributes(self, request):
        """设置实例属性

        :param request: Request instance for ModifyInstanceAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstanceAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstancePre(self, request):
        """预付费实例变配接口，调整磁盘，带宽

        :param request: Request instance for ModifyInstancePre.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstancePreRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyInstancePreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstancePre", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstancePreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPassword(self, request):
        """修改密码

        :param request: Request instance for ModifyPassword.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyPasswordRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRoutineMaintenanceTask(self, request):
        """设置自动化运维属性

        :param request: Request instance for ModifyRoutineMaintenanceTask.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyRoutineMaintenanceTaskRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyRoutineMaintenanceTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoutineMaintenanceTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRoutineMaintenanceTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTopicAttributes(self, request):
        """本接口用于修改主题属性。

        :param request: Request instance for ModifyTopicAttributes.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.ModifyTopicAttributesRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.ModifyTopicAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTopicAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTopicAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewCkafkaInstance(self, request):
        """续费Ckafka实例, 目前只支持国内站包年包月实例续费

        :param request: Request instance for RenewCkafkaInstance.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.RenewCkafkaInstanceRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.RenewCkafkaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewCkafkaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewCkafkaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SendMessage(self, request):
        """通过HTTP接入层发送消息

        :param request: Request instance for SendMessage.
        :type request: :class:`tencentcloud.ckafka.v20190819.models.SendMessageRequest`
        :rtype: :class:`tencentcloud.ckafka.v20190819.models.SendMessageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendMessage", params, headers=headers)
            response = json.loads(body)
            model = models.SendMessageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))