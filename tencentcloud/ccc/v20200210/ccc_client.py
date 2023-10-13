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
from tencentcloud.ccc.v20200210 import models


class CccClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'ccc.tencentcloudapi.com'
    _service = 'ccc'


    def BindNumberCallOutSkillGroup(self, request):
        """绑定号码外呼技能组

        :param request: Request instance for BindNumberCallOutSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.BindNumberCallOutSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.BindNumberCallOutSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindNumberCallOutSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BindNumberCallOutSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindStaffSkillGroupList(self, request):
        """绑定座席所属技能组

        :param request: Request instance for BindStaffSkillGroupList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.BindStaffSkillGroupListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.BindStaffSkillGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindStaffSkillGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.BindStaffSkillGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAdminURL(self, request):
        """创建管理端访问链接

        :param request: Request instance for CreateAdminURL.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAdminURLRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAdminURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAdminURL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAdminURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAutoCalloutTask(self, request):
        """创建自动外呼任务

        :param request: Request instance for CreateAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCCCSkillGroup(self, request):
        """创建技能组

        :param request: Request instance for CreateCCCSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCCCSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCCCSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCCCSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCCCSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCallOutSession(self, request):
        """创建外呼会话，当前仅支持双呼，即先使用平台号码呼出到坐席手机上，坐席接听后，然后再外呼用户，而且由于运营商频率限制，坐席手机号必须先加白名单，避免频控导致外呼失败。

        :param request: Request instance for CreateCallOutSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCallOutSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCallOutSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCallOutSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCallOutSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCarrierPrivilegeNumberApplicant(self, request):
        """用于无限频率地呼叫坐席手机

        :param request: Request instance for CreateCarrierPrivilegeNumberApplicant.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateCarrierPrivilegeNumberApplicantRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateCarrierPrivilegeNumberApplicantResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCarrierPrivilegeNumberApplicant", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCarrierPrivilegeNumberApplicantResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExtension(self, request):
        """创建话机账号

        :param request: Request instance for CreateExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExtension", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSDKLoginToken(self, request):
        """创建 SDK 登录 Token。

        :param request: Request instance for CreateSDKLoginToken.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateSDKLoginTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSDKLoginToken", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSDKLoginTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStaff(self, request):
        """创建客服账号。

        :param request: Request instance for CreateStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStaff", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserSig(self, request):
        """创建用户数据签名

        :param request: Request instance for CreateUserSig.
        :type request: :class:`tencentcloud.ccc.v20200210.models.CreateUserSigRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.CreateUserSigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserSig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserSigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteExtension(self, request):
        """删除话机账号

        :param request: Request instance for DeleteExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeleteExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeleteExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteExtension", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteStaff(self, request):
        """删除坐席信息

        :param request: Request instance for DeleteStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DeleteStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DeleteStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStaff", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeActiveCarrierPrivilegeNumber(self, request):
        """查询生效运营商白名单规则

        :param request: Request instance for DescribeActiveCarrierPrivilegeNumber.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeActiveCarrierPrivilegeNumberRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeActiveCarrierPrivilegeNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeActiveCarrierPrivilegeNumber", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeActiveCarrierPrivilegeNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoCalloutTask(self, request):
        """查询自动外呼任务详情

        :param request: Request instance for DescribeAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAutoCalloutTasks(self, request):
        """批量查询自动任务外呼

        :param request: Request instance for DescribeAutoCalloutTasks.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTasksRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeAutoCalloutTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAutoCalloutTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAutoCalloutTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCCCBuyInfoList(self, request):
        """获取用户购买信息列表

        :param request: Request instance for DescribeCCCBuyInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCCCBuyInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCCCBuyInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCCCBuyInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCCCBuyInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCallInMetrics(self, request):
        """获取呼入实时数据统计指标

        :param request: Request instance for DescribeCallInMetrics.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCallInMetricsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCallInMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCallInMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCallInMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCarrierPrivilegeNumberApplicants(self, request):
        """查询单状态

        :param request: Request instance for DescribeCarrierPrivilegeNumberApplicants.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeCarrierPrivilegeNumberApplicantsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeCarrierPrivilegeNumberApplicantsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCarrierPrivilegeNumberApplicants", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCarrierPrivilegeNumberApplicantsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeChatMessages(self, request):
        """获取指定服务记录文本聊天内容，需要先使用查询在线客服记录（DescribeIMCdrs） API 获取服务记录 SessionId。

        文本聊天记录只保存了 1 年内的，1 年之前会自动清理。

        :param request: Request instance for DescribeChatMessages.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeChatMessagesRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeChatMessagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChatMessages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChatMessagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtension(self, request):
        """获取话机信息

        :param request: Request instance for DescribeExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtension", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeExtensions(self, request):
        """查询话机列表信息

        :param request: Request instance for DescribeExtensions.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeExtensionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtensions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtensionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIMCdrList(self, request):
        """获取包括全媒体和文本会话两种类型的服务记录。

        :param request: Request instance for DescribeIMCdrList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIMCdrList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIMCdrListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIMCdrs(self, request):
        """获取包括全媒体和文本会话两种类型的服务记录。

        :param request: Request instance for DescribeIMCdrs.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeIMCdrsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIMCdrs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIMCdrsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNumbers(self, request):
        """查询号码列表

        :param request: Request instance for DescribeNumbers.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeNumbersRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeNumbersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNumbers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNumbersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePSTNActiveSessionList(self, request):
        """获取当前正在通话的会话列表

        :param request: Request instance for DescribePSTNActiveSessionList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribePSTNActiveSessionListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePSTNActiveSessionList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePSTNActiveSessionListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProtectedTelCdr(self, request):
        """获取主被叫受保护的电话服务记录与录音

        :param request: Request instance for DescribeProtectedTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeProtectedTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeProtectedTelCdrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProtectedTelCdr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProtectedTelCdrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSkillGroupInfoList(self, request):
        """获取技能组信息列表

        :param request: Request instance for DescribeSkillGroupInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeSkillGroupInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSkillGroupInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSkillGroupInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaffInfoList(self, request):
        """获取坐席信息列表

        :param request: Request instance for DescribeStaffInfoList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaffInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaffInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStaffStatusMetrics(self, request):
        """获取坐席实时状态统计指标

        :param request: Request instance for DescribeStaffStatusMetrics.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffStatusMetricsRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeStaffStatusMetricsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStaffStatusMetrics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStaffStatusMetricsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelCallInfo(self, request):
        """按实例获取电话消耗统计

        :param request: Request instance for DescribeTelCallInfo.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCallInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelCallInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelCallInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelCdr(self, request):
        """获取电话服务记录与录音

        :param request: Request instance for DescribeTelCdr.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelCdrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelCdr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelCdrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTelSession(self, request):
        """获取 PSTN 会话信息

        :param request: Request instance for DescribeTelSession.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DescribeTelSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTelSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTelSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableCCCPhoneNumber(self, request):
        """停用号码

        :param request: Request instance for DisableCCCPhoneNumber.
        :type request: :class:`tencentcloud.ccc.v20200210.models.DisableCCCPhoneNumberRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.DisableCCCPhoneNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableCCCPhoneNumber", params, headers=headers)
            response = json.loads(body)
            model = models.DisableCCCPhoneNumberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HangUpCall(self, request):
        """挂断电话

        :param request: Request instance for HangUpCall.
        :type request: :class:`tencentcloud.ccc.v20200210.models.HangUpCallRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.HangUpCallResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HangUpCall", params, headers=headers)
            response = json.loads(body)
            model = models.HangUpCallResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyExtension(self, request):
        """修改话机账号(绑定技能组、绑定坐席账号)

        :param request: Request instance for ModifyExtension.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyExtensionRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyExtensionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExtension", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExtensionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyStaff(self, request):
        """修改客服账号

        :param request: Request instance for ModifyStaff.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ModifyStaffResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyStaff", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyStaffResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetExtensionPassword(self, request):
        """重置话机注册密码

        :param request: Request instance for ResetExtensionPassword.
        :type request: :class:`tencentcloud.ccc.v20200210.models.ResetExtensionPasswordRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.ResetExtensionPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetExtensionPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetExtensionPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopAutoCalloutTask(self, request):
        """停止自动外呼任务

        :param request: Request instance for StopAutoCalloutTask.
        :type request: :class:`tencentcloud.ccc.v20200210.models.StopAutoCalloutTaskRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.StopAutoCalloutTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopAutoCalloutTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopAutoCalloutTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindNumberCallOutSkillGroup(self, request):
        """解绑号码外呼技能组

        :param request: Request instance for UnbindNumberCallOutSkillGroup.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UnbindNumberCallOutSkillGroupRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UnbindNumberCallOutSkillGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindNumberCallOutSkillGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindNumberCallOutSkillGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnbindStaffSkillGroupList(self, request):
        """解绑坐席所属技能组

        :param request: Request instance for UnbindStaffSkillGroupList.
        :type request: :class:`tencentcloud.ccc.v20200210.models.UnbindStaffSkillGroupListRequest`
        :rtype: :class:`tencentcloud.ccc.v20200210.models.UnbindStaffSkillGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindStaffSkillGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindStaffSkillGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))